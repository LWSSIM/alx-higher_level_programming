#!/usr/bin/python3
# ...returns a new dictionary with all values multiplied by 2
def multiply_by_2(a_dictionary):
    new_dict = map(lambda x: (x[0], x[1] * 2), a_dictionary.items())
    return dict(new_dict)
