#!/usr/bin/python3
"""Module: A class that inherits from int
"""


class MyInt(int):
    """A child of int
    inverts logical equality operators
    """

    def __init__(self, value):
        """Init method"""
        self.value = value

    def __eq__(self, other):
        """NOT EQUAL hihi"""
        return self.value != other

    def __ne__(self, other):
        """EQUAL"""
        return self.value == other
