#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 13:29:55 2018

@author: Charlie
"""
'''
These exercises are taken from 
https://www.w3resource.com/python-exercises/python-basic-exercises.php

1. Write a Python program to print the following string in a specific format (see the output). 
Sample String : 
    "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, 
    Like a diamond in the sky." 
Output :
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
'''
print("Twinkle, twinkle, little star\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.")

'''
2. Write a program to get information about the Python version I am using
'''

import sys

print ("Python System is:")
print (sys.version)
print ("System version is:")
print (sys.version_info)
print ("Built in module names:")
print (sys.builtin_module_names)

'''
3. Write a Python program to display the current date and time.
Sample Output : 
Current date and time : 
2014-07-05 14:34:14
'''

import datetime

now = datetime.datetime.now()
print (now)

'''
4. Write a Python program which accepts the radius of a circle from the user and computes the area. 
Sample Output : 
r = 1.1
Area = 3.8013271108436504
'''

import math

radius = float(input("What is the radius of the circle?"))

Area = math.pi * radius
print ("Circle area is", Area)

'''
5. Write a Python program which accepts the user's first and last name and prints them in reverse order 
with a space between them.
'''

first_name = input("What is your first name?")
surname = input ("Now tell me your last name?")

print (surname, first_name)

'''
6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate 
a list and a tuple with those numbers. 
Sample data : 3, 5, 7, 23
Output : 
List : ['3', ' 5', ' 7', ' 23'] 
Tuple : ('3', ' 5', ' 7', ' 23')
'''  

numbers = input("Give me some numbers separated by commas")

list_nums = numbers.split(' ')
tuple_nums = tuple(list_nums)

print (list_nums, tuple_nums)

'''
7. Write a Python program to accept a filename from the user and print the extension of that. 
Sample filename : abc.java 
Output : java
'''
users_file = input("Give me a filename with extension: ")
print ("Name of extension: ", users_file.split('.')[-1])

'''
8. Write a Python program to display the first and last colors from the following list. 
color_list = ["Red","Green","White" ,"Black"]
'''

color_list = ["Red","Green","White" ,"Black"]
print (color_list[0], color_list[3])

'''
9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). 
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
'''
exam_st_date = (11, 12, 2014)
print ("The examination will start from: %i / %i / %i" %exam_st_date)

'''
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
Sample value of n is 5 
Expected Result : 615
'''
n = int(input("input an integer: "))
n = str(n)
print(int(n) + int(n+n) + int(n+n+n))

















