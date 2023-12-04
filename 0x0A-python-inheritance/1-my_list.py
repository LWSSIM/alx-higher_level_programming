#!/usr/bin/python3
"""Module: a class inheritence example (list)
"""


class MyList(list):
    """inhertis from the list class

    Args:
        list (obj):

    Methods:
        __init__: init the class attributes
        print_sorted: prints the list sorted (unmutable)
    """

    def print_sorted(self):
        """Prints list but sorted (ascending sort)"""
        slist = sorted(self)
        print(slist)
