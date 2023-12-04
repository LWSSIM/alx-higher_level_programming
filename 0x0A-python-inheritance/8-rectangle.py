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
    """

    def __init__(self, width, height):
        """set child attributes

        Args:
            width: rect dimensions
            height: rest dimensions
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

        self._width = width
        self._height = height
