#!/usr/bin/python3
# replace item in list copy
def new_in_list(my_list, idx, element):
    copy = my_list[:]
    if idx < 0 or idx > len(my_list) - 1:
        return (copy)
    copy[idx] = element
    return (copy)
