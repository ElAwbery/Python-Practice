#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 20:50:49 2018

@author: ElAwbery
"""
'''
21. Write a Python function to convert a given string to all uppercase if it contains at least 2 
uppercase characters in the first 4 characters. 
'''
def convert_string(string):
    """
    If string contains at least 2 uppercase characters in the first 4 characters, returns string uppercase
    """
    count = 0
    if len(string) < 4:
        return("String not long enough, must be more than 4 characters")
    else:
        for char in string[:4]:
            if char.upper() == char:
                count += 1
        if count > 1:
            return string.upper()
        
    return string

print(convert_string('UPpercase'))
print(convert_string('upperCAse'))



'''
22.Write a Python program to sort a string lexicographically. 
'''
def lexicographistring(string):
    """
    returns string sorted lexicographically
    """
    return ''.join(sorted(list(string)))
    
print(lexicographistring('dkwh2osghe1ighekslqql5sight'))


'''
23. Write a Python program to remove a newline in Python. 
'''

test = '   Python \n'
test2 = '  Python      '

print(test.rstrip())    # rstrip returns a copy of string, without trailing whitespace
print (test)
print(test2.rstrip())


'''
24. Write a Python program to check whether a string starts with specified characters. 
'''

test = '0143902slgks'
test2 = 'fjdsklfdskl'

def check_chars(string, chars):
    """
    checks whether a string starts with particular characters, returns True if it does, False if not
    """
    index = len(chars)
    if string[:index] == chars:
        return True
    
    return False
    
    
test = '0143902slgks'
test2 = 'fjdsklfdskl'

print (check_chars(test, '01'))
print (check_chars(test2, '01'))


'''
25. Write a Python program to create a Caesar encryption. 
'''
def Caesar_encrypt (string, num):
    """
    string is plaintext
    num is an integer 
    returns ciphertext rotated by num
    """
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    cipher = ''
    for char in string:
        
        if char in alphabet_lower:
            index = (alphabet_lower.index(char) + num) % 26
            cipher += alphabet_lower[index]
            
        elif char in alphabet_upper:
            index = (alphabet_upper.index(char) + num) % 26
            cipher += alphabet_upper[index ]
            
    return cipher
 
print (Caesar_encrypt('IBM', -1))
print (Caesar_encrypt('halal', 3))
print (Caesar_encrypt('SecretCodeIsIBM', -1))
print (Caesar_encrypt('RdbqdsBncdHrHAL', 1))
print (Caesar_encrypt('wxyzWXYZ', 4))
print (Caesar_encrypt('abcdABCD', -4))


'''
26. Write a Python program to display formatted text (width=50) as output. 
'''
import textwrap

lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur mattis risus eu sapien maximus, in consequat turpis tempus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec facilisis nibh sit amet arcu faucibus, eget dapibus nisi tempus. Curabitur libero orci, blandit quis urna vel, efficitur feugiat erat. Etiam tristique neque leo, ut sagittis lorem pulvinar ut. Duis iaculis lacus nec mauris scelerisque condimentum. Integer mattis turpis in pellentesque efficitur. Donec scelerisque auctor tincidunt. Fusce a dignissim enim, nec congue ex. Praesent at."

print(textwrap.fill(lorem_ipsum, width = 50))


'''
27. Write a Python program to remove existing indentation from all of the lines in a given text. 
'''
lorem_wrapped = textwrap.fill(lorem_ipsum, width = 50)
lorem_ipsum = lorem_wrapped.replace('\n', '\n    ')
print("Indented: \n", lorem_ipsum)

lorem_ipsum = """
    Lorem ipsum dolor sit amet, consectetur adipiscing
    elit. Curabitur mattis risus eu sapien maximus, in
    consequat turpis tempus. Pellentesque habitant
    morbi tristique senectus et netus et malesuada
    fames ac turpis egestas. Donec facilisis nibh sit
    amet arcu faucibus, eget dapibus nisi tempus.
    Curabitur libero orci, blandit quis urna vel,
    efficitur feugiat erat. Etiam tristique neque leo,
    ut sagittis lorem pulvinar ut. Duis iaculis lacus
    nec mauris scelerisque condimentum. Integer mattis
    turpis in pellentesque efficitur. Donec
    scelerisque auctor tincidunt. Fusce a dignissim
    enim, nec congue ex. Praesent at.
    """

lorem_ipsum = textwrap.dedent(lorem_ipsum)
print(lorem_ipsum)

'''
28. Write a Python program to add a prefix text to all of the lines in a string. 
'''
print(textwrap.indent(lorem_ipsum, '\n \_^:|:^_/'))


'''
29. Write a Python program to set the indentation of the first line. 
'''
lorem_ipsum = textwrap.fill(lorem_ipsum, initial_indent = '    ', subsequent_indent = ' ')
print (lorem_ipsum)

























