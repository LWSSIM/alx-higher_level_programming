#!/usr/bin/python3
"""Module: Base class for the project
"""


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
