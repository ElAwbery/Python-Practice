#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 13:22:39 2018

@author: Charlie
"""
'''
Enumerate all the playing cards in a 52-card deck (no jokers). 
Program should print A♣, 2♣, …, J♣, Q♣, K♣, A♦, …, A♥, …, K♠.
'''


def card_deck():
    """
    Returns all the playing cards in a 52 card deck (no jokers)
    """
    card_string = ''
    
    for suit in '♣♦♥♠':
        for a in 'A23456789JQK':
            card_string += a + suit + ', '
    
    return card_string
    
    
'''
Considering two-card hands, to keep the problem size manageable, enumerate:

* All straight flushes, i.e. pairs of two cards from the same suit in sequential order
'''

def straight_flushes():
    """
    Returns all possible straight flush pairs in a 52 card deck
    """
    flush_list = []
    
    for suit in '♣♦♥♠':
        indx = 0
        for a in 'A23456789JQK':
            card1 = a + suit
            decrement_set = '23456789JQKA'
            card2 = decrement_set[indx] + suit
            indx += 1
            flush_pair = (card1, card2)
            flush_list.append(flush_pair) 
    
    return flush_list
    
'''
* All two-of-a-kinds, i.e. pairs of two cards with the same rank from different suits
'''

def two_of_kind():
    """
    Returns all pairs of two cards with the same rank
    """
    pairs_list = []
    suits = ['♣','♦','♥','♠']
    count =0
    for num in 'A23456789JQK':
        count+=1
        for suit in'♣♦♥♠':
            count+=1
            card1 = num + suit
            temp_suits = suits[:]
            temp_suits.remove(str(suit))
            for indx in temp_suits:
                count+=1
                card2 = num + indx
                pair = (card1, card2)
                pairs_list.append (pair)
    print("count=", count)
    return pairs_list

#an alternate, cleaner version of two-of-a-kind:
  
    
def two_of_kind2():
    """
    Returns all pairs of two cards with the same rank, omits repeat pairs
    """
    pairs_list = []
    suits = ['♣','♦','♥','♠']
    count = 0
    for num in 'A23456789JQK':
        count +=1
        for suit1 in suits:
            count +=1
            for suit2 in suits:
                count+=1
                if suit1 != suit2:
                    pair = (num + suit1, num + suit2)
                    duplicate = (num + suit2, num + suit1)
                    if duplicate not in pairs_list:
                        pairs_list.append(pair)
    print ("count=", count)        
    return pairs_list

'''   
This algorithm works, but its time complexity is n^4 which would cause an efficiency issue
in a generalization. How would you re-write the procedure to have the same time complexity 
as two_of_kind()?
'''
#Solution using cloned list

def two_of_kind3():
    
    pairs_list = []
    rank = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suits = ['♣','♦','♥','♠']
    
    for rank in rank:
        suits2 =suits[:]
        for suit1 in suits:
            card1 = rank + suit1
            
            for suit2 in suits2[1:4]:
                card2 = rank + suit2
                pair = (card1, card2)
                pairs_list.append (pair)
            suits2 = suits2[+1:4]
            
    return pairs_list

#This solution can be generalized into a pattern for iterating unordered pairs (combinations)

def unordered_pairs(list):
   result = []
   sublist = list
   
   for first in list:
       sublist = sublist[1:]
       for second in sublist:
           pair = (first, second)
           result.append(pair)
   return result




def two_of_kind4():
    
    pairs_list = []
    
    ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suits = ['♣','♦','♥','♠']
    subsuits = suits
    
    for rank in ranks:
        
        for first in suits:
            subsuits = subsuits[1:]
            
            for second in subsuits:
                card1 = rank + first
                card2 = rank + second
                pair = (card1, card2)
                pairs_list.append(pair)
        
        subsuits = suits
        
    return pairs_list


            


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
            
          
    
    
    
    
    
    
    
    
