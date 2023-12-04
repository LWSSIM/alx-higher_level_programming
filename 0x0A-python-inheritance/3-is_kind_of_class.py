#!/usr/bin/python3
"""Module: check if inctance or subclass
"""


def is_kind_of_class(obj, a_class):
    """the object is an instance of,
    or if the object is an instance of a class that
    inherited from, the specified class

    Args:
        obj: checked object.
        a_class: specified class.

    Returns:
       bool: The return value. True for success, False otherwise.
    """
    return isinstance(obj, a_class)
