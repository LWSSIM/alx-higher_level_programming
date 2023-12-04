#!/usr/bin/python3
"""Module: is this type of a class
"""


def is_same_class(obj, a_class):
    """is the object is exactly an instance of the
    specified class

    Args:
        obj: checked object.
        a_class: specified class.

    Returns:
       bool: The return value. True for success, False otherwise.
    """
    return type(obj) == a_class
