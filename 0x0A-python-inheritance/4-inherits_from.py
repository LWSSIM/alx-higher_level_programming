#!/usr/bin/python3
"""Module: is this a subclass
"""


def inherits_from(obj, a_class):
    """is the object is an instance of a class that
    inherited (directly or indirectly) from the
    specified class

    Args:
        obj: checked object.
        a_class: specified class.

    Returns:
       bool: The return value. True for success, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
