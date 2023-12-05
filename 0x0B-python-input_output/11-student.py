#!/usr/bin/python3
"""Module: simple class + to_json
"""


class Student:
    """simple example

    Note:
        how to export class to json

    Attrs:
         first_name:
         last_name:
         age:

    Methods:
        __init__: init the class attributes
        to_json: dict rep. of instance
        reload_from_json: replaces all attributes of the
        Student instance
    """

    def __init__(self, first_name, last_name, age):
        """init attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance

        Note:
            -If attrs is a list of strings,
            only attribute names contained in this list must be retrieved.
            -Otherwise, all attributes must be retrieved

        Args:
            attrs: list of attrs to fetch

        Return:
            json(dict format)
        """
        dic_rep = {}

        if isinstance(attrs, list):
            for i in attrs:
                if not isinstance(i, str):
                    break
                if hasattr(self, i):
                    dic_rep[i] = getattr(self, i)
            return dic_rep

        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        Note:
            assumumption: json will always be a dictionary


        Args:
            param1 (int): The first parameter.
            param2 (str): The second parameter.

        Returns:
           bool: The return value. True for success, False otherwise.
        """
        for key in json:
            setattr(self, key, json[key])
