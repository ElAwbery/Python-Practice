#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 14:53:52 2018

@author: ElAwbery
"""

'''
11. Write a Python program to remove the characters which have odd index values of a given string. 
'''

def remove_odd_chars(string):
    """
    Removes all characters with odd index values from a string
    """
    new_string = ''
    while len(string) > 0:
        new_string += string[0]
        string = string[2:]
    return new_string

test_string = 'abcdefghijklmnopqrstuvwxyz'
print(remove_odd_chars(test_string))
print(test_string)



'''
12. Write a Python program to count the occurrences of each word in a given sentence. 
'''
def count_word(sentence):
    """
    sentence is a string of words
    returns a dictionary with words as keys, values as frequencies
    """
    word_count = {}
    words = sentence.split(' ')
    for word in words:
        word_count.setdefault(word, 0)
        word_count[word] += 1
    return word_count

print(count_word('In this sentence there are many words, though I am not sure how many of them are repetitions of previous words. Maybe we will see from this little program whether there are repetitions or not. Also I am aware that this is not one sentence. Oh well.'))



'''
13. Write a Python script that takes input from the user and displays that input back in 
upper and lower cases.
'''

text = input("Write something.")
text = text.upper() + text.lower()
print (text)


''' 
14. Write a Python program that accepts a comma separated sequence of words as input 
and prints the unique words in sorted form (alphanumerically). 
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,
'''

items = input("Input comma separated sequence of words")
words = items.split(", ")
print (', '.join(sorted(list(set(words)))))


'''
15. Write a Python function to create an HTML string with tags around the word(s). 
Sample function and result : 
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
'''
def add_tags(str1, str2):
    """
    Assumes two strings as input
    creates an html tag out of the first string and wraps the second string
    Returns one string of wrapped html
    """
    opening_tag = '<'+str1 + '>'
    closing_tag = '<' + '/'+str1+'>'
    return opening_tag + str2 + closing_tag

print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))


'''
16. Write a Python function to insert a string in the middle of a string. 
Sample function and result : 
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
'''
def insert_string_middle(str1, str2):
    """
    returns a string with second string insterted into the middle of the first string
    """
    index_insert = int(len(str1)/2)
    return str1[:index_insert]+str2+str1[index_insert:]

print(insert_string_middle('[[]]', 'Python'))
print(insert_string_middle('{{}}', 'PHP'))
print(insert_string_middle('<<>>', 'HTML'))


'''
17. Write a Python function to get a string made of 4 copies of the last two characters of a specified 
string (length must be at least 2). 
Sample function and result : 
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses
'''
def repeat_last2(string):
    """
    string length must be longer than 2 characters
    Returns a string of the last two characters * 4
    """
    return string[-2:]*4

print(repeat_last2('python'))
print(repeat_last2('mugglydug'))

'''
18. Write a Python function to get a string made of the first three characters of a specified string. 
If the length of the string is less than 3 then return the original string. 
Sample function and result : 
first_three('ipy') -> ipy
first_three('python') -> pyt
'''
def first_three(string):
    """
    Returns a string of the first three characters of string
    If string is less than 3 characters in length, returns the original string
    """
    if len(string) < 3:
        return string
    return string[:3]

print (first_three('Python'))
print(first_three('spooook'))
print (first_three('12'))


'''
19. Write a Python program to get the first part of a string before a specified character. 
https://www.w3resource.com/python-exercises
https://www.w3resource.com/python
'''
def cut_string_off(string, char):
    """
    Returns string before char, cuts off end of string from char
    """
    index = string.index(char)
    return string[:index]

print(cut_string_off('https://www.w3resource.com/python-exercises', '-'))


'''
20. Write a Python function that reverses a string if its length is a multiple of 4. 
'''

def string_reverse_fours(string):
    """
    If string length is a multiple of 4, reverses the string
    Otherwise returns original string
    """
    if len(string)%4 == 0:
        return ''.join(reversed(string))
    else: 
        return string

print (string_reverse_fours('1234'))
print (string_reverse_fours('onetwothreefour'))
