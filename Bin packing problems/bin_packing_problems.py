#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 14:28:25 2018

@author: Charlie
"""

'''
first_fit(items, bin_size) takes a list of integers, representing the sizes of items to fit in bins. 
The items can be no greater than bin_size. The procedure returns a list of lists. 
Each entry in the top-level list represents a bin. The bin is represented as a list of integers, 
taken from the items argument, that are “packed" into the bin. 
The sum of the list must be no greater than bin_size.

first_fit processes the items argument in the order given. For each item, 
it attempts to place the item in the first bin that can accommodate the item 
(i.e. the first one such that the sum of the items already in the bin, plus the item being processed, 
is <= bin_size). If no existing bin has enough room, first_fit creates a new bin 
(a new bin-list added to the top-level list of bins) and puts the item in the new bin.

eg: first_fit([8, 3, 9, 1, 4, 2, 5, 7], 10) => [[8,1], [3,4,2], [9], [5], [7]]

The following was added as one line into the above code:
Now implement first_fit_decreasing (explained in https://en.wikipedia.org/wiki/Bin_packing_problem#Analysis_of_approximate_algorithms ). 
This just sorts the input in decreasing order, and then does first_fit.

first_fit_decreasing([8, 3, 9, 1, 4, 2, 5, 7], 10) = first_fit([9, 8, 7, 5, 4, 3, 2, 1], 10) 
=> [[9, 1], [8, 2], [7, 3], [5, 4]]

 
'''
#given the spec, this is the best runtime complexity available as far as I can tell. 
#worst case scenario: one item per bin at a runtime of O(n^2)

def first_fit(items, bin_size):
    """
    Takes a list of integers, all no greater than bin_size, also an integer.
    Returns a list of lists, the sum of each list is no greater than bin_size.
    The lists represent the optimal allocation of items to space given the bin-size restriction.
    """
    #check input: if an item is greater than bin_size, terminate program, let user know
    for item in items:
        if item > bin_size:
            return print ("unidentified object in bagging area: your item is too big for our bins.")
    #sort items into reverse order to save runtime
    items.sort(reverse = True)
    #Set up the list of lists
    list_of_bins = [[]]
    
    #For each integer in the list of items
    for item in items:
        item_not_stored = True
        
        while item_not_stored:
        
        #Check to see if it will fit into the first bin, if not, traverse the list of bins until space
           for list_ in list_of_bins:
               #if there is space in the bin, store the item there
               if item + sum(list_) <= bin_size:
                   list_.append(item)
                   item_not_stored = False
                   #stop item from repeated storing in later bins:
                   break
           #if there is no space remaining in any extant bins, create a new bin and add to list_of_bins:
           if item_not_stored:
               new_bin = [item]
               list_of_bins.append(new_bin)
               item_not_stored = False
    
    return list_of_bins

first_fit([8, 3, 9, 1, 4, 2, 5, 7], 10)


'''
Now try modified_first_fit_decreasing 
(described at the end of https://en.wikipedia.org/wiki/Bin_packing_problem#First-fit_algorithm ). 
For this, you might want to go with a bin_size of 12 to get the 1/2, 1/3, and 1/6 bin sizes 
to come out as integers.

Modified first fit decreasing improves on FFD for items larger than half a bin 
by classifying items by size into four size classes large, medium, small, and tiny, 
corresponding to items with size > 1/2 bin, > 1/3 bin, > 1/6 bin, and smaller items respectively. 
Then it proceeds through five phases:
    
Allot a bin for each large item, ordered largest to smallest.

Proceed forward through the bins. On each: If the smallest remaining medium item does not fit, 
skip this bin. Otherwise, place the largest remaining medium item that fits.

Proceed backward through those bins that do not contain a medium item.
 
On each: If the two smallest remaining small items do not fit, skip this bin.
Otherwise, place the smallest remaining small item and the largest remaining small item that fits.

Proceed forward through all bins. 
If the smallest remaining item of any size class does not fit, 
skip this bin. Otherwise, place the largest item that fits and stay on this bin.
Use FFD to pack the remaining items into new bins.
'''


def fits_in_bin(item, list, bin_size):
    """
    checks whether there is space in a bin for a random sized bundle or item
    """
    if item + sum(list) <= bin_size:
        return True
    else:
        return False
    

def modified_first_fit_decreasing(items, bin_size):
    """
    Takes a list of integers, all no greater than bin_size, also an integer.
    Items are sorted into four classes relative to bin_size
    Returns a list of lists, the sum of each list is no greater than bin_size.
    """
    # check input: if an item is greater than bin_size, terminate program, let user know
    for item in items:
        if item > bin_size:
            return print ("unidentified object in bagging area: your item is too big for our bins.")
        
    # sort the items into size classes
    large = []
    medium = []
    small = []
    tiny = []
    
    
    for item in items:
                      
        if item >= bin_size/2:
            large.append(item)
            
        elif item >= bin_size/3:
            medium.append(item)
           
        elif item >= bin_size/6:
            small.append(item)
            
        else:
            tiny.append(item)
            
    list_of_bins = []
    
    # allot a bin for each large item, ordered largest to smallest
    large.sort()                                                    # large list ascendng from here
    
    for item in large[:]:                                       
        list_of_bins.append([item])                                 # large list is now empty
        large.remove(item)
        # Could have appended items to new large then deleted items from old large, but this mirrors the phisical reality
    
    medium.sort()                                                   # medium list ascending from here 
    
    # check if the smallest remaining medium item will fit into a bin
    for bin_ in list_of_bins:
        if medium == []:
            break
        # if the smallest medium sized item will fit into a bin
        elif fits_in_bin (min(medium), bin_, bin_size):
            # place the largest remaining medium item that fits.
            medium.reverse()                                        # medium list descending from here           
            for item in medium:
                if fits_in_bin(item, bin_, bin_size):
                    bin_.append(item)
                    medium.remove(item)
                    
    # sort small items in ascending order 
    small.sort()                                                    # small list ascending from here 
    list_of_bins.reverse()                                          # list_of_bins descending from here
    
    # Proceed backward through those bins that do not contain a medium item
    for bin_ in list_of_bins:
        if small == []:
            break
        elif len(small) >= 2:
            # bins not containing a medium item have only one large item
            if len(bin_) == 1:
                # if the two smallest remaining items fit into a single-item bin
                # place the smallest remaining small item and the largest remaining small item that fits.
                if fits_in_bin(small[0] + small[1], bin_, bin_size):
                    bin_.append (small[0])   # smallest remaining small item
                    
                    #largest remaining small item:
                    small[1:].reverse()                               # small list descending from here
                    for item in small:
                        if fits_in_bin(item, bin_, bin_size):
                            bin_.append(item)
                            small.remove(item)
                                                          
    # If the two smallest remaining small items do not fit, traverse to next bin - no else clasue needed 
    
    list_of_bins.sort()
    tiny.sort()                                                       # tiny list ascending from here
    # amalgamate all remaining items
    remaining_items = tiny + small + medium + large
    
    # Proceed forward through all bins
    for bin_ in list_of_bins:
        # if the smallest remaining item does fit in a bin
        if fits_in_bin (remaining_items[0], bin_, bin_size):
            remaining_items.reverse()                                 # remaining items descending from here
            for item in remaining_items:
                if fits_in_bin(item, bin_, bin_size):
                    bin_.append(item)
                    remaining_items.remove(item)
                    break
            # skip the bin if the smallest item does not fit (no else clause)    
            break   
    # now stay on this bin
    list_of_bins.append (first_fit(remaining_items, bin_size))
    print(list_of_bins)
    return list_of_bins


modified_first_fit_decreasing([8, 3, 9, 1, 4, 2, 5, 7], 12)
















    
