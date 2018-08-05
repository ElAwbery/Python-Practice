#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 20:05:57 2018

@author: ElAwbery
"""

'''
Write a function called nested_sum that takes a list of lists of integers and adds up the elements 
from all of the nested lists. 

For example:
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21
'''

def nested_sum(list):
    """
    Takes one list with nested lists that have integer elements
    Returns the sum of all elements in the nested lists
    """
    adder = 0
    for el in list:
        adder += sum(el)
    
    return adder

integer_lists = [[1,2], [3,5,8], [0], [7,0,6], [], [4]]

#It’s unnecessary (and inefficient) to build another list. Can you write this 
#without allocating any memory in the loop?

'''
Write a function called cumsum that takes a list of numbers and returns the cumulative sum; 
that is, a new list where the ith element is the sum of the first i + 1 elements from the original list. For example:
>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
'''

def cumsum(list):
    """
    Takes an arithmetic sequence as list of integers, returns the arithmetic series of the sequence
    (the cumulative sums of sequence elements)
    """
    list_of_cumulatives = []
    adder = 0
    for i in range(len(list)):
        num = list[i]
        adder += num
        list_of_cumulatives.append(adder)
        
    return list_of_cumulatives

        
arithmetic_sequence = [5, 8, 0, 45, 782, 5, 1, 11]


'''
Write a function called middle that takes a list and returns a new list that contains 
all but the first and last elements. 
For example:
>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]
'''

def middle_list(list):
    """
    takes a list and returns the list with its first and last elements removed
    """
    return list[1:-1]


'''
Write a function called chop that takes a list, modifies it by removing the first and
last elements, and returns None. 
For example:
>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3]
'''

def chop(list):
    """
    Takes a list and removes the first and last elements of the list.
    Returns None.
    """
    list.remove(list[0])
    return list.remove(list[-1])
    
'''
Write a function called is_sorted that takes a list as a parameter and returns 
True if the list is sorted in ascending order and False otherwise. 
For example:
>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False
'''  
#is_sorted using a for loop
def is_sorted(list):
    """
    Takes a list of elements, returns True if they are assorted in ascending order, False if not.
    """
    
    for el in range(0, len(list)-1):

        if type(list[el]) != type(list[el+1]):
            print("list contains elements of incomparable types")
            return False
        elif not list[el] < list[el+1]:
            return False

    return True

sorted_list = [0, 1, 2, 3, 6, 9, 356]
sorted_list2 = ['a', 'c', 'f', 'i']
unsorted_list = [76, 3, 8]
empty_list = []
unsorted_list2 = ['c', 0, 'b', 3, 'b', 4]

#is_sorted using a while loop
def is_sorted2(list):
    """
    Takes a list of elements, returns True if they are assorted in ascending order, False if not.
    """
    
    comparison_list = list[:]
    i = 0
    
    while True:
        if len(list)==0:
            print("list is empty")
            return True
        if not list[i] < comparison_list[i+1]:
            return False
        elif i == len(list)-2:
            return True
        i +=1

    






















