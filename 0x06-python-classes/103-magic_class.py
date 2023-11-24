#!/usr/bin/python3
"""
Module: attempt to convert Python ByteCode
"""
import math


class MagicClass:
    """
    class: magic class

    Note:
        converted from bytes code

    Methods:
        __init__: init the class attributes
    """

    def __init__(self, radius=0):
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """
        Calculates the area of a circle
        """
        return self.__radius**2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of a circle
        """
        return self.__radius * 2 * math.pi
