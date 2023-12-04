#!/usr/bin/python3
"""Module: BaseGeo Class + methods
"""


class BaseGeometry:
    """
    class:

    Note:
        this class has no class attributes

    Methods:
        area: raise exception
    """

    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validor of passed value

        Args:
            name: str:
            value: int: to be checked

        Raises:
           Type:
           Value:
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
