#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:22:26 2018

@author: ElAwbery
"""

'''
This is an alternate answer to the relative primes qustion, using the Python library built in module

Enumerate all relatively prime pairs of integers between 2 and the input number n. 
Two integers are relatively prime if there is no integer greater than one that divides them both 
(that is, their greatest common divisor is one). 
For example, 12 and 13 are relatively prime, but 12 and 14 are not.
'''

from math import gcd

def primePairs (n):
    
    low = 2
    relPrimeList = []
    
    while low < n:
        for a in range (low, n+1):
            if gcd(n, a) == 1:
                pair = (a, n)               # make a pair
                relPrimeList.append (pair)  # add pair to rel prime list
        n -= 1
    return relPrimeList


