#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 15:08:07 2018

@author: ElAwbery
"""

#Write a function that returns a string written backwards

def backward_written_string(str):
    """
    Takes a string and returns the string written backwards
    """
    n = len(str)-1
    backwards_string = ''
    
    while n >= 0:
        backwards_string += str[n]
        n -= 1
        
    return backwards_string




#Write a function that returns a string written backwards, use a while loop with a break clause:

def backward_written_string2(str):
    """
    Takes a string and returns the string written backwards
    """
    n = len(str)-1
    backwards_string = ''
    while True:
        if n < 0:
            break
        
        backwards_string += str[n]
        n -= 1
        
    return backwards_string


#Write a function that returns a string written backwards, use a for loop:
    

def backward_written_string3(str):
    """
    Takes a string and returns the string written backwards
    """
    
    backwards_string = ''
    
    for letter in str:
        backwards_string = letter + backwards_string
    
    return backwards_string
        
        
    
