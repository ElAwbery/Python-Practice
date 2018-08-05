#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 17:15:04 2018

@author: ElAwbery
"""
'''
Taken from various versions on Stack Overflow
'''
    
'''
Use a while loop to print a triangle of asterisks, like this: 
    
    *
   ***
  *****
 *******
*********

'''
count = 0
asterisks_low = 5
asterisks_high = 5
characters_in_row = 10
row = ""

while count < 5:
    for character in range(characters_in_row):
        if character >= asterisks_low and character <= asterisks_high:
            row += '*'
        else: 
            row += ' '
    print (row)
    count += 1
    asterisks_low -= 1
    asterisks_high += 1
    row = ""
    
    
'''
Write a function that prints a triangle of asterisks like the one in the previous question. 
The function should accept a single parameter, height, that defines how tall the triangle is 
(in the previous example height = 5). Use a while loop and ensure your function works by trying 
different heights.
'''

def asterisks_triangle(height):
    """
    Assumes height is an integer representing number of rows desired
    Prints a triangle of asterisks containing rows of height specification
    eg: if height = 9, there are 9 rows in the triangle
    """
    count = 0
    characters_in_row = (height*2)-1
    asterisks_low = int(characters_in_row/2)
    asterisks_high = int(characters_in_row/2)
    row = ""

    while count < height:
        for character in range(characters_in_row):
            if character >= asterisks_low and character <= asterisks_high:
                row += '*'
            else: 
                row += ' '
        print (row)
        count += 1
        
        asterisks_low -= 1
        asterisks_high += 1
        row = ""
        
    
test1 = asterisks_triangle(7)
test2 = asterisks_triangle(10)
test3 = asterisks_triangle(24)

'''
When the condition for the while loop requires a lot of code, it is sometimes more readable 
to loop forever and explicitly use the break keyword. Fix the following code to do this:
'''    
attempts = 0
while True :
    response = input("Do you want to quit? (y/n): ") 
    attempts += 1
    
    if response == 'y':
        break
    
    print("Exiting after", attempts, "attempts")

    
        
