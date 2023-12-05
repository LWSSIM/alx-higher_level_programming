#!/usr/bin/python3
"""Module: functions that adds attributes
"""


def add_attribute(obj, name, value):
    """adds and attribute and it's value,
    when possible

    Args:
        obj:
        name:
        value:
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
