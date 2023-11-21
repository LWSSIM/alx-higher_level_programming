#!/usr/bin/python3
"""
Module: create class Square with attributes
"""


class Square:
    """
    class:
        Square

    Note:
        this class has no class attributes
    Args:
        size (int): of the square
    Methods:
        __init__: init the class atrbt
    """

    def __init__(self, size=0):
        """
        Init an instance of class Square raise some exeptions
        with msg

        Args:
            input new square size(private instance attribute)
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size
