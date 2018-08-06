#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 14:24:28 2018

@author: Charlie
"""
'''
Source for these exercises:
https://www.w3resource.com/python-exercises/python-functions-exercises.php
'''
'''
1. Write a Python function to find the max of three numbers. 
'''
def find_max_of_three(n1, n2, n3):
    """
    Assumes n1, n2 and n3 are integers or floats
    returns the number with the maximum value
    """
    return max(n1, n2, n3)

print (find_max_of_three(3, 4, 5))
print (find_max_of_three(-3, 3, 3.897))

'''
2. Write a Python function to sum all the numbers in a list. 
Sample List : [8, 2, 3, 0, 7]
Expected Output : 20 
'''
def sum_elements(list):
    """
    Assumes list is a list of numbers, ints or floats
    Returns the sum of the numbers in the list
    """
    return sum(list)

print(sum_elements([8, 2, 3, 0, 7]))

'''
3. Write a Python function to multiply all the numbers in a list. 
Sample List : [8, 2, 3, -1, 7]
'''
def product_elements(list):
    """
    Assumes list is a list of integers or floats
    Returns the product of all the numbers in the list
    """
    product = 1
    for element in list:
        product *= element
    
    return product

print(product_elements([8, 2, 3, -1, 7]))


'''
4. Write a Python program to reverse a string. 
Sample String : "1234abcd"
Expected Output : "dcba4321"
'''
def reverse_string(string):
    """
    Returns a new string containing the elements of string in reverse order
    """
    reverse_string = ''
    
    for item in range(0, len(string)):
        reverse_string += string[-1]
        string = string[:-1]
    
    return reverse_string

print("reverse_string=", reverse_string("1234abcd"))

'''
5. Write a Python function to calculate the factorial of a number (a non-negative integer). 
The function accepts the number as an argument. 
'''
def efficient_factorial(num):
    """
    Num is a non-negative integer
    Returns the factorial of num
    """
    
    
    if num in factorials:
        return factorials[num]
    else:
        answer = num*(efficient_factorial(num-1))
        factorials[num] = answer
        print (factorials)
        return answer

factorials = {1:1,}

print("factorial result =", efficient_factorial(8))

'''
6.Write a Python function to check whether a number is in a given range. 
'''
def in_range(num, x, y):
    """
    Num is a float or integer
    x and y are integers
    Returns True if x>=num<=y, False otherwise
    """
    
    if num >= x and num <= y:
        return True
    return False
    
    
print(in_range(6.7, 3.1, 7))
print(in_range(6.7, 7, 10))
# alternate version for pre-defined range:

def in_range_0to10(num):
    """
    assumes num is a float or integer
    Returns True if num is in range 0 - 10
    """
    if num in range(0, 10):
        return True
    
    return False

print(in_range_0to10(5))
print(in_range_0to10(-1))


'''
7. Write a Python function that accepts a string and calculate the number of upper case letters and 
lower case letters. 
Sample String : 'The quick Brown Fox'
Expected Output : 
No. of Upper case characters : 3
No. of Lower case Characters : 13
'''
def uppers_lowers_count(string):
    """
    Prints number of upper case letters and lower case letters in input string
    """
    upper_count = 0
    lower_count = 0
    
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    counts = (upper_count, lower_count)
    print("No. of upper case characters:", counts[0])
    print("No. of lower case characters:", counts[1])
    
     
uppers_lowers_count('The quick Brown Fox')


'''
8. Write a Python function that takes a list and returns a new list with unique elements of the first list. 
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
'''
print(list({1, 2, 3, }))

def get_unique_elements(list_):
    """
    Returns a list of only the unique elements in list
    """
    
    return list(set(list_))
    

print(get_unique_elements([1,2,3,3,3,3,4,5]))


'''

9. Write a Python function that takes a number as a parameter and check the number is prime or not. 

Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors 
other than 1 and itself. 
'''


def prime_detector(num):
    """
    Returns True if num is prime, False otherwise
    """
    if num == 0 or num == 1 or num == 2:
        return False
    
    else:
        for int in range(2, num):
            if num % int == 0:
                return False
    
    return True

print(prime_detector(101))

print(prime_detector(287))


'''
10. Write a Python program to print the even numbers from a given list. 
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] 
Expected Result : [2, 4, 6, 8]
'''

def get_evens(list_):
    """
    list_ is a list of integers
    Returns a new list with only the even ints from list_
    """
    
    evens = []
    for int in list_:
        if int%2 ==0:
            evens.append(int)
            
    return evens

print(get_evens([1, 2, 3, 4, 5, 6, 7, 8, 9] ))

