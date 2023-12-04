#!/usr/bin/python3
"""Module: Child of base_geom class
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Child subclass

    BaseGeometry:
        parent class

    Method:
        __init__:
        area:
        __str__:
    """

    def __init__(self, width, height):
        """set child attributes

        Args:
            width: rect dimensions
            height: rest dimensions
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self._width = width
        self._height = height

    def area(self):
        """implement area for this subclass"""
        return self._width * self._height

    def __str__(self):
        """print and str methods"""
        return f"[Rectangle] {self._width}/{self._height}"
