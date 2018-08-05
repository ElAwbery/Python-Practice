#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 13:23:44 2018

@author: ElAwbery
"""

'''
These exercises are taken from 
https://www.w3resource.com/python-exercises/python-basic-exercises.php
'''

'''
21. Write a Python program to find whether a given number (accept from the user) is even or odd, 
print out an appropriate message to the user.
'''

user_num = int(input("Give me an integer"))

if user_num%2 == 0:
    print("This is an even number")
    
else:
    print ("This is an odd number")
    
'''
22. Write a Python program to count the number 4 in a given list.
'''

def count_4(list):
    """
    Counts how many times the number 4 appears in a list
    """
    count = 0
    for element in list:
        if element == 4:
            count += 1
    return count

print(count_4([1, 4, 6, 7, 4]))
print(count_4([1, 4, 6, 4, 7, 4]))



'''
23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters 
of a given string. Return the n copies of the whole string if the length is less than 2.
'''

def copy_string_spec(string, n):
    """
    n is a non-negative integer
    Returns n copies of the first 2 characters of string
    If length of string is less than 2, returns n copies of the whole string
    """
    if len(string)>=2:
        return string[:2] * n
    return string * n

print (copy_string_spec('abcabcabc', 2))
print (copy_string_spec('?', 5))
print (copy_string_spec (' .py', 3))


'''
24. Write a Python program to test whether a passed letter is a vowel or not. 
'''

def is_vowel(letter):
    """
    assumes letter is a character, upper or lower case
    returns True if the letter is a vowel
    """
    vowel = 'aeiouAEIOU'
    
    return letter in  vowel

print(is_vowel('A'))
print(is_vowel('i'))
print(is_vowel('?'))
print(is_vowel('t'))
print(is_vowel('0'))
print(is_vowel('u'))
   

'''
25. Write a Python program to check whether a specified value is contained in a group of values. 
Test Data : 
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
 '''
 
def contains_value(value, list):
    """
    Takes an object and a list of values of any type
    Returns True if the object is in the list, False otherwise
    """
    return value in list

print (contains_value(3, [1, 5, 8, 3]))
print (contains_value(-5, [1, 5, 8, 3]))
print (contains_value('hi', [1, 8, [4,5, 'Hi']]))
print (contains_value(['hello', 4], [1, 5, ['hello', 4], 8, 3]))


'''
26. Write a Python program to create a histogram from a given list of integers.
'''

def histogram (list):
    """
    Assumes list is a list of integers
    Returns a pictoral representation of integers as frequencies
    """
    for int in list:
        counter = ''
        while int > 0:
            counter += '*'
            int -= 1
        print (counter)
    

histogram([1, 2, 1, 2, 3, 6, 5, 7, 7, 7, 4, 8, 34])



'''
27. Write a Python program to concatenate all elements in a list into a string and return it.
'''
def list_to_string(list):
    """
    Turns a list into a string and returns the string
    """
    string = ''
    for el in list:
        string += str(el)
    return string

print (list_to_string ([1, 2, 'foo', 2, 3, 'hippy', 5, 'hi', 7, 7, 4, 8, 34]))


'''
28. Write a Python program to print all even numbers from a given numbers list in the same order 
and stop the printing of any numbers that come after 237 in the sequence. 
'''

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

for number in numbers:
    if number%2 == 0:
        print(number)
    elif number == 237:
        break

'''
29. Write a Python program to print out a set containing all the colors from color_list_1 which 
are not present in color_list_2. 
Test Data 
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
Expected Output : 
{'Black', 'White'}
'''

color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])

print(color_list_1 - color_list_2)

'''
30. Write a Python program that will accept the base and height of a triangle and compute the area.
'''
    
b = int(input("Input the base : "))
h = int(input("Input the height : "))

area = b*h/2

print("area = ", area)





































   
    

