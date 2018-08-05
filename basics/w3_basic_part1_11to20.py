#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 13:39:04 2018

@author: Charlie
"""

'''
These exercises are taken from 
https://www.w3resource.com/python-exercises/python-basic-exercises.php
'''
'''
11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
Sample function : abs()
Expected Result : 
abs(number) -> number
Return the absolute value of the argument.
'''
# This is how to print out the docstring of a built-in function
# Remember that you need double underscores, not single ones
print(abs.__doc__)
print(int.__doc__)



'''
12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
'''
import calendar

year = int(input("give me a year: "))
month = int(input("now give me a month (as an integer): "))

print (calendar.month(year, month)) 



'''
13. A 'heredoc' in other languages is a multi-line string literal that preserves whitespace and line breaks.
In Python you can just print the whitespace as you prefer using tripple quotes. 
Line breaks will be kept
'''

print ("""
       A string that you don't have to escape. 
       This
       is a .......multi-line
       heredoc string example
       """) 



'''
14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''

import datetime 

date1 = (input("Give me a year, month and day: "))
date2 = (input("Give me another year, month and day: "))


date1 = date1.split(' ')
date2 = date2.split(' ')

year1 = int(date1[0])
month1 = int(date1[1])
day1 = int(date1[2])

year2 = int(date2[0])
month2 = int(date2[1])
day2 = int(date2[2])

date1 = datetime.date(year1, month1, day1)
date2 = datetime.date(year2, month2, day2)

days_between_dates = date2 - date1
print("Days difference: ", days_between_dates.days)



'''
15. Write a Python program to get the volume of a sphere with radius 6.
'''
import math

pi = math.pi

r = 6

volume = 4/3 * pi * r**3

print (volume)



'''
16. Write a Python program to get the difference between a given number and 17, 
if the number is greater than 17 return double the absolute difference. 
'''
def strange_difference(x):
    
    difference = abs(17 - x)

    if x > 17:
        return 2*difference
    else:
        return difference
    
print (strange_difference(22))
print (strange_difference(14))



'''
17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
'''

def close_enough(x):
    """
    assumes x is a number, int or float
    if x is within 100 of 1000 or 2000, returns True, otherwise returns False
    """
    return abs(1000 - x) <= 100 or abs(2000 - x) <= 100
        

print (close_enough(1000))
print (close_enough(900))
print (close_enough(800))
print (close_enough (2600))



'''
18. Write a Python program to calculate the sum of three given numbers, 
if the values are equal then return thrice of their sum. 
'''

def sum_of_three(x, y, z):
    """
    assumes x, y, and z are ints or floats
    if they are all equal, returns thrice their sum
    """
    if x == y == z:
        return 9*x  # 3 * x+x+x = 9 * x
    else:
        return x + y + z
    
print (sum_of_three(1, 2, 3))
print (sum_of_three( 3, 3, 3))
print (sum_of_three(1.0, 1.0, 1))
print (sum_of_three(1.4, 5.6, 7.8))



'''
19. Write a Python program to get a new string from a given string where "Is" has been added to the front. 
If the given string already begins with "Is" then return the string unchanged.
'''

def new_string(string):
    """
    Takes a string and returns a new string with 'Is' added to the front, unless the string already
    begins with 'Is'in which case, returns original string
    """
    if string[:2] == 'Is':
        return string
    
    return 'Is' + string
    
print (new_string ('Isabelle'))
print (new_string (' this a thing?'))
print (new_string (''))



'''
20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.
'''

def string_copies(string, n):
    """
    Assumes n is a non-negative integer
    Returns n copies of string
    """
    return n * string

print (string_copies('Hello', 6))







































