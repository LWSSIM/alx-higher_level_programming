#!/usr/bin/python3
# find if list items are divisable by 2 return list of (T/F)
def divisible_by_2(my_list=[]):
    bool_list = []
    i = 0
    while i < len(my_list):
        bool_list.append(True if my_list[i] % 2 == 0 else False)
        i += 1
    return (bool_list)
