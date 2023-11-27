#!/usr/bin/python3
"""Class Rectangle
"""


class Rectangle:
    """Defines a rectangle

        Attributes:
            width: int
            height: int

        Properties:
            def width(self): setter + getter
            def height(self): setter + getter
    """
    def __init__(self, width=0, height=0):
        """initialize Rectangle

        Args:
            width: input rectangle width (optional)
            height: input rectangle height (optional)
                both args are defaulted to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width attr

            Return:
                width private attr
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width

            Args:
                value: desired width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter for the height attr

            Return:
                height private attr
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height

            Args:
                value: desired height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
