#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 14:36:42 2018

@author: Charlie
"""
'''
histogram() takes a string and counts how many times each letter appears
'''
def histogram_original(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1 
        else:
            d[c] += 1
    return d

'''
Use get to write histogram more concisely. You should be able to eliminate the if statement.
'''

def histogram(word):
    """
    input: word is a string
    returns a dictionary with letters in word for keys, number of occurrancies per letter as values
    """
    letter_counter = dict()
    for letter in word:
        letter_counter[letter] = letter_counter.get(letter, 0)+1
    return letter_counter

'''
Dictionary practice importing a text file of words. All the words in words.txt are in in one string,
separated by a space.

Write a function that reads the words in words.txt and stores them as keys in a dictionary. 
It doesn’t matter what the values are. Then you can use the in operator as a fast way 
to check whether a string is in the dictionary.
'''
    
fin = open('words.txt', 'r')

text = fin.readline()

def myWords(text):
    """
    text is a single string of words
    returns word_dictionary, each word of string is a key in word_dictionary
    """
    word_dictionary = dict()
    for word in text.split(' '):            # words of text are split into separate strings
        word_dictionary[word] = 0
    return word_dictionary
       

myDictionary = myWords(text)

'''
If key is in the dictionary setdefault(key, [default]) returns its value. 
If not, setdefault(key, [default]) insert key with a value of default and returns the default. 
Default defaults to None.

Use setdefault to write a concise version of invert_dict()
'''

def invert_dict(dict):
    """
    Takes a dictionary. Assigns its values to keys in a new dictionary.
    Stores multiple keys with same values from the old dictionary in lists 
    Returns the new dictionary.
    """
    inverse = {}
    for key in dict:
        val = dict[key]
        # set key and value using setdefault
        # setdefault returns dict value (or empty list if non yet assigned)
        inverse.setdefault(val, []).append(key) # creates a new key if val is not yet a key
        
    return inverse

# test invert_dict()
parrot_dict = histogram('parrot')
parrot_inverse = invert_dict(parrot_dict)

'''
Memoize the Ackermann function (see: https://en.wikipedia.org/wiki/Ackermann_function)
and see if memoization makes it possible to evaluate the function with bigger arguments. 
Hint: no.
'''

def ackermann(m, n):
    """
    takes two non-negative integers m and n
    computes the Ackermann-Peter function
    """

    if m == 0:
        return n + 1 
    elif m > 0 and n == 0:
        return ackermann(m-1, 1)  
    return ackermann(m-1, ackermann(m, n-1))

    
print (ackermann (0, 0))

'''
def ackermann_memoized(m, n):
    """
    takes two non-negative integers m and n
    computes the Ackermann-Peter function
    stores already computed values in a dictionary, keys are tuples (m, n)
    """
    ackermann_dict = {(0,0):1}
    
    if (m, n) in ackermann_dict:
        return ackermann_dict[(m, n)]
    elif m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann_memoized(m-1, 1)
    else:
        ackermann_dict[(m, n)] = ackermann_memoized(m-1, ackermann_memoized(m, n-1))
    
    print(ackermann_dict)
    return ackermann_dict
'''

def ackermann2(m, n):
    """Computes the Ackermann function A(m, n)

    See http://en.wikipedia.org/wiki/Ackermann_function

    n, m: non-negative integers
    """
    ackermann_dict = {}
    if m == 0:
        return n+1
    if n == 0:
        return ackermann2(m-1, 1)

    if (m, n) in ackermann_dict:
        return ackermann_dict[m, n]
    else:
        ackermann_dict[m, n] = ackermann2(m-1, ackermann2(m, n-1))
        return ackermann_dict[m, n]

    
print(ackermann2(3, 4))

'''
has_duplicates takes a list and returns True if there is any element that appears more than once. 
It should not modify the original list.
Use a dictionary to write a faster, simpler version of has_duplicates.
'''

def has_duplicates(list):
    """
    Takes a list
    Returns True if the list includes any element that appears more than once
    Original list is not modified.
    """
    seen = {}
    for el in list:
        if el in seen:
            return True
        else:
            seen[el] = 1
    return False

print(has_duplicates ([1, 3, 5, 6, 1, 8, 5, 0]))
print(has_duplicates ([]))
print(has_duplicates ([0, 1, 2, 3, 4, 5, 6, 7, 8]))
print (has_duplicates (['abc', 'acb', 'adr', 'tut']))
print (has_duplicates (['a', 1, 6, 'b', 3, 'abc', 1.0]))

'''
Write a program that reads a wordlist and finds all the rotate pairs.
'''
# myDictionary variable created near top of file, dic with words as keys


            
    

    
    
   















































    