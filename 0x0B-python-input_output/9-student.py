#!/usr/bin/python3
"""Module: simple class + to_json
"""


class Student:
    """simple example

    Note:
        how to export class to json

    Attr:
         first_name:
         last_name:
         age:

    Methods:
        __init__: init the class attributes
        to_json: dict rep. of instance
    """

    def __init__(self, first_name, last_name, age):
        """init attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
