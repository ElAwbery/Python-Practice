#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 13:36:57 2018

@author: Charlie
"""

'''
1. Write a Python program to calculate the length of a string. 
'''
print(len('google.com'))


'''
2. Write a Python program to count the character frequency in a string. 
Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''
def character_count(string):
    """
    Counts the character repetitions in a string
    Returns a dictionary with keys as characters, values as frequencies
    """
    frequencies = {}
    for character in string:
        frequencies.setdefault(character, 0)
        frequencies[character] += 1
        
    return frequencies

print(character_count('google.com'))


'''
3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
If the string length is less than 2, return instead the empty string. 
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
'''
def first_last_two(string):
    """
    Takes a string and returns a new string containing the first two and last two characters of the original string
    If the original string is less than two characters in length, returns an empty string
    """
    if len(string) < 2:
        return ''
    return string[:2] + string[-2:]
    
print (first_last_two('w3resource'))
print (first_last_two('w3'))
print (first_last_two('w'))
print (first_last_two(''))


''' 
4. Write a Python program to get a string from a given string where all occurrences of its first char 
have been changed to '$', except the first char itself. 
Sample String : 'restart'
Expected Result : 'resta$t'
'''

def dollar_string(string):
    """
    Takes a string and returns a new_string with $ in place of repeats of the first character
    """
    dollar_string = string[0]
    first = string[0]
    for char in string[1:]:
        if char == first:
            dollar_string += '$'
        else: 
            dollar_string += char
    return dollar_string

print (dollar_string('restart'))

# A better solution:

def dollar_string2(string):
    """
    Takes a string and returns a new_string with $ in place of repeats of the first character
    """
    first = string[0]
    dollar_string = first + string[1:].replace(first, '$')
    return dollar_string

print (dollar_string2('restart'))   


'''
5. Write a Python program to get a single string from two given strings, separated by a space 
and swap the first two characters of each string. 
Sample String : 'abc', 'xyz' 
Expected Result : 'xyc abz'
'''

def mix_strings(str1, str2):
    """
    Takes two strings, returns one string composed of the two strings separated by a space
    The first two characters of each string are swapped
    """
    return str2[:2] + str1[2:] + ' ' + str1[:2] + str2[2:]
    
print(mix_strings('abc', 'xyz'))
print(mix_strings('fjdksl;afd sl', '0143829748923789'))


'''
6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead. 
If the string length of the given string is less than 3, leave it unchanged. 
Sample String : 'abc'
Expected Result : 'abcing' 
Sample String : 'string'
Expected Result : 'stringly'
'''
def add_ing(string):
    """
    Assumes a string input of at least three characters
    Returns a string with 'ing' added to the original string
    If the input string already ends in 'ing' returns a string with 'ly' added
    """
    if len(string) < 3:
        return string
    elif string[-3:] == 'ing':
        return string + 'ly'
    return string + 'ing'

print(add_ing('abc'))
print(add_ing('p'))
print(add_ing('string'))
print (add_ing('You are procrastinat'))
print(add_ing('ping'))



'''
7. Write a Python program to find the first appearance of the substring 'not' and 'good' from a given string, 
if 'good' follows the 'not', replace the whole 'not'...'good' substring with 'good'. 
Return the resulting string. 
Sample String : 'The grammar is not that good!'
Expected Result : 'The grammar is good!'
'''
def not_poor(str1):
  wd_not = str1.find('not')
  wd_good = str1.find('good')

  if wd_good > wd_not:
    str1 = str1.replace(str1[wd_not:(wd_good+4)], 'good')

  return str1

print(not_poor('The grammar is not that good!'))
print(not_poor('The grammar is dreadful'))
print(not_poor('The grammar is bad'))



'''
8. Write a Python function that takes a string of words and returns the length of the longest one. 
'''

def longest_word(string):
    """
    Takes a string of words and spaces
    Returns the length of the longest word
    """
    word_list = string.split(' ')
    max_count = 0
    
    for word in word_list:
        if len(word) > max_count:
            max_count = len(word)
            
    return max_count
        
print(longest_word('This is a string with some words longer than others and longest is the longest word.'))


'''
9. Write a Python program to remove the nth index character from a nonempty string. 
'''

def remove_index(string, n):
    """
    Assumes string is not empty and n is an integer
    Returns new string with the nth index character removed
    """
    if n+1 > len(string):
        return "string has no index number n"
    return string[:n] + string[n+1:]

print(remove_index('abcdeffghijk', 5))
print(remove_index('abcdeffghijk', 2))
print(remove_index('abcdeffghijk', 0))
print(remove_index('abcdeffghijk', 10))
print(remove_index('abcdeffghijk', 12))


'''
10. Write a Python program to change a given string to a new string where the first and last chars 
have been exchanged. 
'''
def exchange_first_last(string):
    """
    Takes a string and returns new string with first and last characters swapped
    """
    return string[-1]+string[1:-1]+string[0]

print(exchange_first_last('mbcdefghijkla'))































