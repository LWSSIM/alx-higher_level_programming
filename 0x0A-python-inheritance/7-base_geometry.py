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
        integer_valitaor: validates input
    """

    def area(self):
        """raise exception
        area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validor of passed value

        Args:
            name: (str)
            value: (int) to be checked

        Raises:
           Type:
           Value:
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
