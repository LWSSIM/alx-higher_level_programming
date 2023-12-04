#!/usr/bin/python3
"""Module: Fn to get information about an obj
"""


def lookup(obj):
    """function that returns the list of
    available attributes and methods of an object

    Args:
        obj: passed object

    Return:
        List containing all the info above
    """
    return dir(obj)
