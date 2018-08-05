#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 15:25:23 2018

@author: ElAwbery
"""
'''
Enumerate all positive rational numbers: 1/1, 1/2, 2/1, 1/3, 3/1, 2/3, 3/2, 1/4, 4/1, 2/4, 4/2, 
3/4, 4/3, 1/5, …

This list is infinite. For convenience, you may want the program to take an argument n 
and only print the first n elements in the sequence.
'''
#This is a solution to the above problem which takes an input which is max for the numerator

def allRationals (n):
    """
    Takes an integer, n and returns all rationals between 1/1 and n
    """
    low = 1
    while low < n:
        for a in range (low, n):
            rat1 = str(a) + '/' + str(n)
            rat2 = str(n) + '/' + str(a)
            print (rat1, rat2)
        n -= 1
        

'''
The pattern of the allRationals output is different to that in the problem spec. 
 
The enumeration in the problem spec lists all rationals using numerator and denominator both up to k, 
and then all the ones (that are not duplicates) up to k+1, and so on.
 
So for any given rational like 246209/896229 it will eventually get there on the 896229th time around 
its outer loop, if allowed to run indefinitely.

A different input is needed to solve for the enumeration pattern in the problem spec. 
Rather than a max for the numerator/denominator, the input n will force halting 
so you don’t have to manually abort it.

To do this, the looping structure needs to be a bit different to the first solution.
'''
from math import gcd

def allRationals2(n):
    """
    Takes an integer n and returns the first n rationals in a very specific order
    For each new integer input, every smaller integer in ascending order is divided by the new integer 
    and then divides the new integer (denominator then numerator)
    """
    list_of_rats = [1]
    int_point = 2
    list_of_ints =[1]
    
    while len(list_of_rats) < n:
        
        for el in list_of_ints:                     #el will be numerator then denominator
            for el2 in list_of_ints:                #el2 will be denominator then numerator)
                
                rat1 = str(el)+'/'+str(el2)
                if el==1:                           #eliminates 1 from denominators
                    rat2 = str(el2)
               
                rat2 = str(el)+'/'+str(el2)
                
                list_of_rats.append(rat1)
                list_of_rats.append(rat2)
                      
                int_point += 1
        list_of_ints.append(int_point)
    
    return list_of_rats
        
            
'''
Versions: 

a) print the numbers as strings with / in them, as shown
'''
def allRationals3 (n):
    """
    Takes an integer, n and returns all rationals between 1/1 and n as a string
    """
    low = 1
    ratString = ''
    while low < n:
        for a in range (low, n):
            rat1 = str(a) + '/' + str(n)
            rat2 = str(n) + '/' + str(a)
            ratString = ratString + rat1 + ', ' + rat2 + ', '
        
        n -= 1
    print (ratString)
    
'''
b) do the division, so they are printed 1, 1/2, 2, 1/3, 3, 2/3, …
'''
def allRationals4 (n):
    """
    Takes an integer, n and returns all rationals between 1/1 and n as a string
    """
    low = 1
    ratString = ''
    while low < n:
        for a in range (low, n):
            if a == 1:
                rat2 = str(n)
            else:
                rat2 = str(n) + '/' + str(a)
            rat1 = str(a) + '/' + str(n)
            ratString = ratString + rat1 + ', ' + rat2 + ', '
        
        n -= 1
    print (ratString)

    
'''  
c) eliminate duplicates, so a number appears in the sequence only once. For example, 
    2/4 would divide to 1/2 which has already appeared once, so it shouldn’t appear again
'''
from math import gcd

def allRationals5 (n):
    """
    Takes an integer, n and returns all rationals between 1/1 and n as a string
    """
    low = 1
    ratString = ''
    
    while low < n:
        for a in range (low, n):
            
            while gcd(a, n) > 1:
                div = gcd(a, n)
                a = int(a/div) 
                n = int(n/div)
                
            if a == 1:
                rat2 = str(n) 
            
            else:
                rat2 = str(n) + '/' + str(a)
                
            rat1 = str(a) + '/' + str(n)
            
            if n == 1:
                rat1 = str(a)
                
            ratString = ratString + rat1 + ', ' + rat2 + ', '
        
        n -= 1
    print (ratString)


