#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 17:22:15 2018

@author: ElAwbery
"""
'''
Enumerate all relatively prime pairs of integers between 2 and the input number n. 
Two integers are relatively prime if there is no integer greater than one that divides them both 
(that is, their greatest common divisor is one). 
For example, 12 and 13 are relatively prime, but 12 and 14 are not.
'''
      
#relPrime function uses the Euclidean computation for greatest common denominator:

'''
1: If a<b, exchange a and b (unecessary step when working with an ordered sequence)
2: Divide a by b and get the remainder, r. 
3: If r=0, report b as the GCD of a and b.
4: Replace a by b and replace b by r. 
5: Repeat from step 3
''' 

def primePairs (n):
    
    low = 2
    relPrimeList = []
    
    while low < n:
        for a in range (low, n+1):
            if relPrime (n, a):
                pair = (a, n)               # make a pair
                relPrimeList.append (pair)  # add pair to rel prime list
        n -= 1
    return relPrimeList


def relPrime (a, b):
    """
    takes two integers a and b, a is always larger than b
    returns true if a and b are relative primes
    (that is, if their greatest common denominator == 1)
    """
    if a%b == 1:
        return True
    elif a%b == 0:
        return False
    else:
        r = a%b
        a = b
        b = r
        relPrime (a, b)
