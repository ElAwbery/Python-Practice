#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 12:20:04 2018

@author: ElAwbery
"""

'''
Enumerate the domino pairs in a set of dominoes with max number of dots n,
without using the binomial coefficient
'''

def domino_pairs(n):
    """
    n is an integer, the max number of dots per side of a domino pair
    returns a list of all pairs in the set and the number of dominos in a set
    """
    domino_list = []
    number_in_set = 0
    for side1 in range(n+1):         #n+1 because blanks are included
        for side2 in range(n+1):
            pair = (side1, side2)
            duplicate = (side2, side1)
            if duplicate not in domino_list:
                domino_list.append(pair)
                number_in_set += 1
    domino_set = (number_in_set, domino_list)
    return domino_set
    
                
'''           
This algorithm has a time complexity issue - it could be made faster.
The problem is that by the end of the iteration through elements in the second for loop,
all the pairs except one will test as duplicates and be removed
Here is another attempt: 
'''

def domino_pairs2(n):
    """
    n is an integer, the max number of dots per side of a domino pair
    returns a list of all pairs in the set and the number of dominos in a set
    """
    domino_list = []
    number_in_set = 0
    
    for side1 in range(n+1):         #n+1 because blanks are included
        
        for side2 in range(side1, n+1):  
            pair = (side1, side2)
            domino_list.append(pair)
            number_in_set += 1
        
    domino_set = (number_in_set, domino_list)
    return domino_set


