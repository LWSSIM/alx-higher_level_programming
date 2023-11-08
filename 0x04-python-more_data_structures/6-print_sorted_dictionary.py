#!/usr/bin/python3
# ...prints a dictionary by ordered keys.
def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        print(f'{key}: {value}')
