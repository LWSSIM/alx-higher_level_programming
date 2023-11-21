#!/usr/bin/python3
"""
Module: define a square (class) init it and define other methods
Note:
    size is a private attribute.
    @setter will centralize the logic.
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
        Init method for  an instance of class Square -raise some
        exeptions with msg

        Args:
            input new square size(private instance attribute)
        """
        self.size = size

    @property
    def size(self):
        """
        Retrives size attribute

        Args:
            none

        Returns:
           int: size of Square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        sets size attribute

        Args:
            size (int)
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        calc current square area

        Args:
            none

        Returns:
            int: area of the square(size**2)
        """
        return self.__size**2

    def my_print(self):
        """
        print the Square with '#'

        Args:
            None
        """
        if not self.size:
            print()
        for i in range(self.size):
            print("#" * self.size)
