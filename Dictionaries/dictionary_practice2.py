#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 15:05:50 2018

@author: Charlie
"""
'''
These problems are taken from: 
http://wasabiapp.org/python_course/exercises_4.pdf
'''

d = { "key1":1, "key2":2, "key3":1, "key4":3, "key5":1, "key6":4, "key7":2 }
'''
for k in d :
    print("key=", k, " value=", d[k], sep = "")
'''    
# modify the code above to print just the keys associated with values that are greater than 1
    
for k in d :
    if d[k] > 1:
        print("key=", k, " value=", d[k], sep = "")
        
    
'''
Write a function called accept login(users, username, password) with three parameters: 
users: a dictionary of username keys and password values, 
username: a string for a login name and password a string for a password. 
The function should return True if the user exists and the password is correct and False otherwise. 
'''

users = {
    "user1" : "password1",
    "user2" : "password2",
    "user3" : "password3"
}
  
def accept_login(users, username, password):
    """
    Assumes users is a dictionary of username keys and password values
    Assumes username is a string 
    Assumes password is a string
    Returns True if user is in users and password is correct, and False otherwise
    """
    if username in users:
        return users[username] == password
    
    
# Here is the calling code, test your code with both good and bad passwords as well as 
# non-existent login names: 
        
if accept_login(users, "wronguser", "wrongpassword"): 
    print("login successful!")    
else:
    print("login failed...")


if accept_login(users, "user2", "passwordXXX"):
    print("login successful!")
else:
    print("login failed...")

    
if accept_login(users, "user2", "password2"):
    print("login successful!")
else:
    print("login failed...")


'''
Write a function called find value(mydict, val) that accepts a dictionary called mydict 
and a variable of any type called val. The function should return a list of keys 
that map to the value val in mydict.
'''

def find_value(mydict, val):
    """
    Assumes mydict is a dictionary
    Assumes val is a variable of any type
    Returns a list of keys that map to val in mydict
    """
    val_keys = []
    for key in mydict:
        if mydict[key] == val:
            val_keys.append(key)
    
    return val_keys

users = {
    "user1" : "password1",
    "user2" : "password2",
    "user3" : "password3",
    "user4" : "password2",
    "user5" : "password2",
    "user6" : "password1",
    "user7" : "password2",
    "user8" : "password3",
    "user9" : "password1",
    "user10" : "password2",
    "user11" : "password1",
    "user12" : "password2",
    "user13" : "password3",
}    

print(find_value(users, 'password3'))

'''
Write a function to invert a dictionary. It should accept a dictionary as a parameter 
and return a dictionary where the keys are values from the input dictionary and the values 
are lists of keys from the input dictionary. For example, this input:
    { "key1" : "value1", "key2" : "value2", "key3" : "value1" }
should return this dictionary:
    { "value1" : ["key1", "key3"], "value2" : ["key2"] }
'''

def dict_invert(dict):
    """
    Assumes a dictionary as input
    Returns a dictionary that has values from the input dictionary for keys
    Any repeated values in the input dictionary become one key in the new dictionary, mapping to 
    a list of values made up of their keys from the input dictionary
    """
    
    inverse_dict = {}
    for key in dict:
        val = dict[key]
        inverse_dict.setdefault(val,[]).append(key)
    
    return inverse_dict

print(dict_invert(users))

'''
Write a function called word frequencies(mylist) that accepts a list of strings called mylist 
and returns a dictionary where the keys are the words from mylist and the values 
are the number of times that word appears in mylist:
    
word_list = list("aaaaabbbbcccdde")
word_freq = { ’a’ : 5, ’b’ : 4, ’c’ : 3, ’d’ : 2, ’e’ : 1 }

if word_frequencies(word_list) == word_freq : 
    print("correct")

else : 
    print("wrong")
'''

def word_frequencies(mylist):
    """
    Assumes mylist is a list of strings
    Returns a counter dictionary with words from mylist as keys and frequencies as values
    """
    word_freq = {}
    for word in mylist:
        word_freq.setdefault(word, 0)
        word_freq[word] += 1
        
    
    return word_freq


word_list = list("aaaaabbbbcccdde")

print (word_frequencies(word_list))

'''
In bioinformatics a k-mer is a substring of k characters from a string that is longer than k 
(see https://en.wikipedia. org/wiki/K-mer for details). 
Write a function with two parameters: a string containing DNA and the value of k. 
Return a dictionary of k-mer counts.
'''
def k_mer_frequencies(dna, k):
    """
    Assumes input of a string containing DNA
    k is a substring of the string
    Returns number of times k appears in string
    """
    k_mer_counts = {}
    
    while len(dna) >= k:
        k_mer = dna[:k]
        k_mer_counts.setdefault(k_mer, 0)       # add k_mer to dictionary if not yet an entry
        k_mer_counts[k_mer] += 1                # count 1 for this occurrence of k_mer
        dna = dna[1:]                           # move forward one character in the dna string 
      
    return k_mer_counts
    
dna1 = 'AGATCGAGTG'
dna2 = 'GTAGAGCTGT'
 
print(k_mer_frequencies(dna1, 3))
print(k_mer_frequencies(dna1, 2))
print(k_mer_frequencies(dna2, 3))
print(k_mer_frequencies(dna2, 2))   
    

# Here is a recursive version of the same function, just for the hell of it
def k_mer_frequencies2(dna, k, k_mer_counts = {}): 
    """
    Assumes input of a string containing DNA
    k is a substring of the string
    Returns number of times k appears in string
    """
    
    k_mer = ''
        
    if len(dna) == k:       # the last k letters in dna
        k_mer = dna
        k_mer_counts.setdefault(k_mer, 0)
        k_mer_counts[k_mer] += 1
        
        return k_mer
        
    else: 
        k_mer += dna[:k]  # the first k letters in dna  
        k_mer_counts.setdefault(k_mer, 0)       # add k_mer to dictionary if not yet an entry
        k_mer_counts[k_mer] += 1                # count 1 for this occurrence of k_mer
        dna = dna[1:]                           # move forward one character in the dna string 
        k_mer_frequencies2(dna, k, k_mer_counts)
    
    return k_mer_counts



dna1 = 'AGATCGAGTG'
dna2 = 'GTAGAGCTGT'

print(k_mer_frequencies2(dna1, 3, k_mer_counts = {}))
print(k_mer_frequencies2(dna1, 2, k_mer_counts = {}))
print(k_mer_frequencies2(dna2, 3, k_mer_counts = {}))
print(k_mer_frequencies2(dna2, 2, k_mer_counts = {}))






































   
    
    
    
    
    