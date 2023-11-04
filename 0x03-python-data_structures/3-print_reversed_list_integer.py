#!/usr/bin/python3
# prints list items in reverse order
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for item in reversed(my_list):
            print("{:d}".format(item))
