#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 14:34:39 2018

@author: ElAwbery
"""

'''
Problems 1 - 10 from w3resource, lists:
https://www.w3resource.com/python-exercises/list/
'''

'''
1. Write a Python program to sum all the items in a list. 
'''
def items_sum(list):
    """
    Adds the number of items in a list, returns sum 
    """
    count = 0
    for item in list:
        count += 1
        
    return count

testlist = [5, 'ty', 'hello', 5, 6, 7, 000]

print (items_sum(testlist))

# Alternately:

print (len(testlist))


'''
2. Write a Python program to multiply all items in a list of integers. 
'''
def multiply_items(list):
    """
    Assumes list is a list of integers
    Returns product of all integers in list
    """
    sum = 1
    for item in list:
        sum *= item
    return sum

integers = [5, 6, 4, 3, -2]

print(multiply_items(integers))


'''
3. Write a Python program to get the largest number from a list. 
'''
def get_max(list):
    """
    Assumes list contains only numbers
    Returns largest number in list
    """
    max = list[0]
    
    for item in list:
        if item > max:
            max = item
            
    return max

numbers = [5, 6, 4.67, 3, -2, 764, 3.5, 764.43, -789.2]

print(get_max(numbers))


'''

4. Write a Python program to get the smallest number from a list. 
'''
def get_min(list):
    """
    Assumes list contains only numbers
    Returns smallest number in list
    """
    min = list[0]
    
    for item in list:
        if item < min:
            min = item
            
    return min

numbers = [5, 6, 4.67, 3, -2, 764, 3.5, 764.43, -789.2]

print(get_min(numbers))

'''
5. Write a Python program to count the number of strings where the string length is 2 or more 
and the first and last character are same from a given list of strings. 
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''
def count_strings(list):
    """
    List is a list of strings
    counts number of strings in list where string length is greater than 2 and the first and last character
    of each string are the same
    """
    count = 0
    
    for string in list:
        if string[0] == string[-1] and len(string) > 2:
            count += 1
            
    return count

sample = ['abc', 'xyz', 'aba', '1221']
print(count_strings(sample))

sample2 = ['abca', 'xx', '00', '3a3', 'adef']
print(count_strings(sample2))

'''
6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple 
from a given list of non-empty tuples. 
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''
def ordered_tuples(list):
    """
    Assumes list is a list of tuples
    Returns a list with tuple elements sorted by their last element in increaing order
    """
    def last(tuple):
        return tuple[-1]
    
    return sorted(list, key = last)
        
test_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

print(ordered_tuples(test_list))


'''
7. Write a Python program to remove duplicates from a list. 
'''
def remove_duplicates(list):
    """
    Returns a list with no duplicates
    """
    no_dup_list = []
    
    for item in set(list):
        no_dup_list.append(item)
        
    return no_dup_list

duplicates = [0, 0, 'a', 'ab', 'a', 'hi', 78, 4.3, 'hi', 4.3, 'nope', 00, '', '   ']

print(remove_duplicates(duplicates))


'''
8. Write a Python program to check a list is empty or not. 
'''

def is_empty(list):
    """
    Returns True if list is empty, False if not
    """
    return list == []

print(is_empty([]))
print(is_empty([1]))


'''
9. Write a Python program to clone or copy a list. 
'''
print(duplicates.copy())


'''
10. Write a Python program to find the list of words that are longer than n from a given list of words. 
'''
def longer_than_n(list, n):
    """
    Assumes input is a list of words and n is an int
    Returns a list of all words in input list that are longer than n letters
    """
    long_words = []
    for word in list:
        if len(word) > n:
            long_words.append(word)
    return long_words

fames_ac = ['fames', 'ac', 'turpis', 'egestas', 'Donec', 'facilisis', 'nibh', 'sit', 'amet', 'arcu', 'faucibus',]
 
print(longer_than_n(fames_ac, 4))     




































