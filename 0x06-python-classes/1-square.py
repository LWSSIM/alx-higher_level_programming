#!/usr/bin/python3
"""
Module:
    create class Square with attributes
"""


class Square:
    """
    class:
        Square

    Note:
        this class has no class attributes
    Args:
        size of the square <-(int)
    Methods:
        __init__: init the class atrbt
    """

    def __init__(self, size=0):
        """
        Init an instance of class Square

        Args:
            input new square size(private instance attribute)
        """
        self.__size = size
