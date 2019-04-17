# Decorator practice

# 1. Memoization: 

def memoize(func):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = func(x)
            print(memo, x)
        return memo[x]
    return helper

@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# fib = memoize(fib)

print(fib(7))

# 2. Tracing: print call and result. Indent by two spaces in each nested call

def tracer(func):
    """
    Takes a function and runs it
    Prints every call to the function and the return value
    Indents each call and return by two spaces
    """
    name = func.__name__
    tracer.depth = 0
    
    def helper(*args):
        tracer.depth += 1
        call_statement = name + " called with " + str(args)
        indent = '|  ' * tracer.depth
        print (indent + call_statement)
        # keeping the * before args calls the function with as many args as are in the tuple
        result = func(*args)
        print('+' + ' -' * tracer.depth + name + ' ' + str(args) + " is " + str(result))
        tracer.depth -= 1
        return result
    return helper

@tracer
def adder(*args):
    results = []
    for x in args:
        results.append(x+3)
    return results

adder(3, 4, 7)

@tracer
def fib(n):
    if n == 0:    
        return 0
    elif n == 1:  
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib(5)

# 3. Timing: print call, time taken, and result

import time

def timer(func):
    """
    Prints function call, time taken and result
    """
    def helper(*args):
        name = func.__name__
        call_time = time.time()
        result = func(*args)
        result_time = time.time()
        print(name, "called with result ", result)
        print("Time taken was ", result_time - call_time)
        return result
    return helper

@timer
def fib(n):
    if n == 0:    
        return 0
    elif n == 1:  
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib(5)

# 4. Define decorate_multiple(decorator, *function_names) 

import time

def timer(func):
    """
    Prints function call, time taken and result
    """
    def helper(*args):
        name = func.__name__
        call_time = time.time()
        result = func(*args)
        result_time = time.time()
        print(name, "called with result ", result)
        print("Time taken was ", result_time - call_time)
        return result
    return helper

def adder(*args):
    results = []
    for x in args:
        results.append(x+3)
    return results 

def fib(n):
    if n == 0:    
        return 0
    elif n == 1:  
        return 1
    else:
        return fib(n-1) + fib(n-2)

def decorate_multiple(decorator, *function_names):
    """
    Takes a decorator and one or more names of functions
    Applies the decorator to the functions
    Returns the decorated function values
    """
    functions = []
    for name in function_names:
        # globals()[“name"] gets the function object
        func = globals()[name]
        functions.append(func)
    results = []
    for func in functions:
        result = decorator(func)
        results.append(result)
    return results
    
decorate_multiple(timer, 'adder', 'fib')
