#!/usr/bin/python3
# returns the biggest int value of list
def max_integer(my_list=[]):
    if my_list == []:
        return (None)
    my_list.sort()
    return (my_list[-1])
