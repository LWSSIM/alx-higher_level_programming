#!/usr/bin/python3
# ...adds all unique integers in a list (only once for each integer).
def uniq_add(my_list=[]):
    new_set = set(my_list)
    res = sum(i for i in new_set) 
    return res
