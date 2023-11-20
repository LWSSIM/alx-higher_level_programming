#!/usr/bin/python3
# prints the first x elements of a list and only integers
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            n += 1
        except (ValueError, TypeError, IndexError):
            continue
    print()
    return n
