#!/usr/bin/python3
"""Module: function that returns the dictionary
description with simple data structure
"""


def class_to_json(obj):
    """get class dict descritpion
    Note:
        for JSON serialization of obj

    Args:
        my_obj: passed obj isinstance of a class

    Return:
        returns the dictionary description with simple data structure
        i.e: __dict__ method
    """
    return obj.__dict__
