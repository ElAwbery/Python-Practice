#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 13:12:01 2018

@author: ElAwbery
"""
'''
The code in this file cleans up the code in bin_packing_problems, avoiding repetition.
There is a new helper function, bin_pack()

The problem statement: 

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



def first_fit(items, bin_size):
    """
    Takes a list of integers, all no greater than bin_size, also an integer.
    Returns a list of lists, the sum of each list is no greater than bin_size.
    """
    # check input: if an item is greater than bin_size, terminate program, let user know
    for item in items:
        if item > bin_size:
            return print ("unidentified object in bagging area: your item is too big for our bins.")
    # sort items into reverse order to save runtime
    items.sort(reverse = True)
    # Set up the list of lists
    bins = [[]]
    
    # For each integer in the list of items
    for item in items:
        item_not_stored = True
        
        while item_not_stored:
        
        # traverse the bins to find first bin into which item will fit
           for list_ in bins:
               # if there is space in the bin, store the item there
               if item + sum(list_) <= bin_size:
                   list_.append(item)
                   item_not_stored = False
                   # stop item from repeated storing in later bins:
                   break
           # if there is no space remaining in any extant bins, create a new bin and add to bins:
           if item_not_stored:
               new_bin = [item]
               bins.append(new_bin)
               item_not_stored = False
    
    return bins

first_fit([8, 3, 9, 1, 4, 2, 5, 7], 10)



def fits_in_bin(item, list, bin_size):
    """
    checks whether there is space in a bin for a random sized bundle or item
    """
    
    if item + sum(list) <= bin_size:
        return True
    else:
        return False
    
    
# Algorithmic complexity of bin_pack = O(n^2)   
def bin_pack(bins, sizes, item_to_check, bin_size, once_only = False):
    """
    items on sizes (a list of items with size bounds) are efficiently packed into bins in bins
    item_to_check is an integer
    item_to_check is tested for fit
    largest possible item from sizes is packed to bin and removed from sizes
    """
    # Proceed forward through all bins
    
    for bin in bins:
        if sizes == []:
            break
        
        sizes.reverse()
        # clone sizes  so that list is not modified during traverse
        for item in sizes[:]:           
            if fits_in_bin(item, bin, bin_size):
                bin.append(item)
                # remove item from original sizes list, not the cloned one
                sizes.remove(item)
                if once_only == True:
                    return bins, sizes
            
    return bins, sizes 
        

def modified_first_fit_decreasing(items, bin_size):
    """
    Takes a list of integers, all no greater than bin_size, also an integer.
    Items are sorted into four classes relative to bin_size
    Returns a list of lists, the sum of each list is no greater than bin_size.
    The lists represent the optimal allocation of items to space given the bin-size restriction.
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
            
    bins = []
    
    large.sort()                                                    # large list ascendng from here
    # allot a bin for each large item, ordered largest to smallest
    bins = [[item] for item in large]
                                                                    # large list is now empty and not used again  
    medium.sort()                                                   # medium list ascending from here 
    
    bins, medium = bin_pack(bins, medium, medium[0], bin_size)
                   
    # sort small items in ascending order 
    small.sort()                                                    # small list ascending from here 
    bins.reverse()                                                  # list_of_bins descending from here
    
    
    # create list with only large bins in it
    only_large_bins = []
    
    # Traverse those bins that do not contain a medium item
    for bin_ in bins[:]:
        if len(bin_) == 1:
            only_large_bins.append(bin_)
            bins.remove(bin_) # remove large-only bins from list_of_bins to avoid bin doubles later
    
    only_large_bins.reverse()
    only_large_bins, small = bin_pack(only_large_bins, small, small[0]+small[1], bin_size)
    
    bins += only_large_bins  # add the modified large-item bins back to the list_of_bins
    
    tiny.sort()                                                       # tiny list ascending from here
    # amalgamate all remaining items
    remaining_items = tiny + small + medium
   
    # Proceed forward through all bins
    # bin_pack once_only must be true for this call, see problem definition "stay on this bin" 
    bins, remaining_items = bin_pack(bins, remaining_items, remaining_items[0], bin_size, once_only = True)
   
    bins += first_fit(remaining_items, bin_size)
    print("final list of bins", bins)
    return bins

modified_first_fit_decreasing([8, 3, 9, 1, 4, 2, 5, 7], 12)






























