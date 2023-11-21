#!/usr/bin/python3
"""
Module: define a square (class) init it and define other methods
Note:
    size/position are private attributes.
    @getter/setter(properties) to centralize the logic.
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

    def __init__(self, size=0, position=(0, 0)):
        """
        Init method for  an instance of class Square -raise some
        exeptions with msg

        Note:
            uses setter & getter logic
        Args:
            input new square size(private instance attribute)
            input new position tupple(private)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrives size attribute

        Note:
            getter

        Args:
            none

        Returns:
           int: size of Square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        sets size attribute (setter)

        Args:
            size (int)
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """
        position tupple getter

        Args:
            None

        Returns:
           tupple or error
        """
        return self.__position

    @position.setter
    def position(self, position):
        """
        setter for position private attribute

        Error:
            condition for success:
                any i in tupple[2] i > 0
        Args:
            (int)tupple[2]
        """
        if (
            not isinstance(position, tuple)
            or len(position) != 2
            or not isinstance(position[0], int)
            or not isinstance(position[1], int)
            or position[0] < 0
            or position[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
            return

        if self.position[1] > 0:
            print("\n" * self.position[1], end="")

        for i in range(self.size):
            print("_" * self.position[0], end="")
            print("#" * self.size)
