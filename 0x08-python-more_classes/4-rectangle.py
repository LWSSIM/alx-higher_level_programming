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

    def area(self):
        """Method for area calculation

            Returns:
                rectangle area->int
        """
        return self.height * self.width

    def perimeter(self):
        """Method for perimeter calculation

            Returns:
                rectagle perileter->int
        """
        if self.height == 0 or self.width == 0:
            return 0

        return 2 * (self.height + self.width)

    def __str__(self):
        '''str method of the Class

            Return:
                string representing the attributes
                    using the '#' char

            Note:
                retuns None is attrs are 0
        '''
        if self.height == 0 or self.width == 0:
            return ''

        width = self.width
        _print = (('#' * width) + '\n') * self.height
        return _print[:-1]

    def __repr__(self):
        '''repr method of the Class

            Retun:
                expression that can be used by eval
                that can be used to recreate an identical
                instance
        '''
        return 'Rectangle({}, {})'.format(self.width, self.height)
