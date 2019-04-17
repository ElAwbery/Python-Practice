# RealPython.com has excellent training resources on decorators
# https://realpython.com/primer-on-python-decorators/

import functools
import time
import random

# Basic pattern, easy to build on
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator



def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__} in {run_time:.4} secs")
        return value
    return wrapper_timer



def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        # repr() turns object to string
        args_repr = [repr(a) for a in args] 
        # format a string of arguments that are key=value pairs 
        kwargs_repr = [f"{k}={v}" for k, v in kwargs.items()]
        # Join lists of positional and keyword arguments  
        signature = ", ".join(args_repr + kwargs_repr)           
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__} returned {value}")           # 4
        return value
    return wrapper_debug

# slow down function is useful for rate-limiting a function that continuously checks whehter a resource, eg a web page, has changed. The @slow_down decorator sleeps for a second before it calls the decorated function. 

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down


# example is commented out
# PLUGINS is a global dict, shows how the register decorator works
# PLUGINS = dict()

# No wrapper function is needed, the decorator does not wrap a function in this instance, it is simply keeping track of all new plugins in a global dict variable that can be called.
# The example uses random to call a greeting function from the global dic. 
# functools @wraps therefore not needed

# This is a great way of automating a list update
# It effectively hand picks a specified set from globals()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)

# login_required decorator is usually supplied by web frameworks, in which case you would not write your own. 

from flask import Flask, g, request, redirect, url_for
import functools
app = Flask(__name__)

def login_required(func):
    """Make sure user is logged in before proceeding"""
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required

@app.route("/secret")
@login_required
def secret():
    ...

# Calling a decorator with or without arguments

# Remember that 'calling the decorator' is to call the function that has been decorated. 
# This example shows that you can create a decorator that will decorate functions with none or any number of arguments. 

# The function is an optional argument, because either it will be called by the wrapper function or by the top level decorator, depending on whether it takes arguments itself or not. 
# The top level decorator parameters must be sepcified by keyword because its function parameter is optional
# The * syntax is special, meaning all following parameters are keyword only


def name(_func=None, *, kw1=val1, kw2=val2, ...):  
    def decorator_name(func):
        ...  # Create and return a wrapper function.

    # if the decorator is called as a function with arguments, return a wrapper function that can read and return a function. 
    if _func is None:
        return decorator_name 
    # If the decorator is called as a function without arguments, apply the wrapper function immediately
    else:
        return decorator_name(_func)    


# Using a function to track state with an attribute

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        wrapper_decorator.tracker += 1
        print(f"Call {wrapper_decorator.tracker} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_decorator.tracker = 0
    return wrapper_decorator


           