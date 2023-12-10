#!/usr/bin/python3
"""Module: Base class for the project
"""

import json
import csv


class Base:
    """the “base” of all other classes in this project

    Note:
        manage id attribute

    Attr:
        __nb_objects:

    Methods:
        __init__: init the class attributes
    """

    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """Init method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integer_validator(self, name, value):
        """Validor of passed valuus to int

        Args:
            name: (str)
            value: (int) to be checked

        Raises:
           Type:
           Value:
        """
        if value is not None and type(value) is not int:
            raise TypeError(name + " must be an integer")

        if (name == "width" or name == "height") and value <= 0:
            raise ValueError(name + " must be > 0")

        if (name == "y" or name == "x") and value < 0:
            raise ValueError(name + " must be >= 0")

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string rep, for passed
        List of dict
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        str_rep_instance = []
        if list_objs is not None:
            for inst in list_objs:
                str_rep_instance.append(cls.to_dictionary(inst))  # type: ignore
        with open(f"{cls.__name__}.json", "w") as f:
            f.write(Base.to_json_string(str_rep_instance))
