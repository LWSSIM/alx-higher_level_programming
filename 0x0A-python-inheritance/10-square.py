#!/usr/bin/python3
"""Module: Square subclass of rectangle
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """1st child of Rectangle
    2nd child of Rectangle

    Methods:
        __init__:
        area:
        integer_validator:
    """

    def __init__(self, size):
        """init new instance

        Note:
            calls parents init method
            via `super()`

        size: (int)
        """
        self.integer_validator("size", size)
        self._size = size

        super().__init__(size, size)
