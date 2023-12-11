#!/usr/bin/python3
"""Module: Base class for the project
"""

import json
import csv
import turtle
import random


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
                str_rep_instance.append(cls.to_dictionary(inst))
        with open(f"{cls.__name__}.json", "w") as f:
            f.write(Base.to_json_string(str_rep_instance))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation
        """

        L = []
        if json_string is not None and json_string != "":
            L = json.loads(json_string)
        return L

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes
        already set

        Args:
            cls: the class
            dictionary: think a double pointer
                to a dictionary
        """
        if cls.__name__ == "Rectangle":
            temp = cls(1, 1)
        else:
            temp = cls(1)
        cls.update(temp, **dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """returns a list of instances

        Note:
            created from the file from(save_to_file)
        """
        try:
            with open(f"{cls.__name__}.json", "r") as f:
                json_str = cls.from_json_string(f.read())
                inst_list = []
                for item in json_str:
                    inst_list.append(cls.create(**item))
                return inst_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        with open(f"{cls.__name__}.csv", "w") as f:
            write = csv.writer(f)
            for item in list_objs:
                if cls.__name__ == 'Rectangle':
                    write.writerow([item.id, item.width, item.height,
                                    item.x, item.y])
                else:
                    write.writerow([item.id, item.size, item.x, item.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in csv"""
        try:
            with open(f"{cls.__name__}.csv", "r") as f:
                read = csv.reader(f)
                inst_list = []
                keys = [["id", "width", "height", "x", "y"],
                        ["id", "size", "x", "y"]]
                inst_dict = {}
                for item in read:
                    if cls.__name__ == 'Rectangle':
                        for key, value in zip(keys[0], item):
                            inst_dict[key] = int(value)
                    elif cls.__name__ == 'Square':
                        for key, value in zip(keys[1], item):
                            inst_dict[key] = int(value)
                    inst_list.append(cls.create(**inst_dict))
                return inst_list
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares
        Note:
            uses turtle graphic module

        Args:
            list_rectangle: list of Rectangle objects
            list_square: list of Square objects
        """
        t = turtle.Turtle()
        screen = turtle.Screen()
        colors = ["red", "orange", "yellow", "green",
                  "black", "blue", "purple"]
        for rec in list_rectangles:
            t.color(random.choice(colors))
            t.penup()
            t.goto(rec.x, rec.y)
            t.pendown()
            for _ in range(5):
                t.begin_fill()
                t.forward(rec.width)
                t.right(90)
                t.forward(rec.height)
                t.right(90)
                t.end_fill()
            screen.clear()
        for sqr in list_squares:
            t.color(random.choice(colors))
            t.penup()
            t.goto(sqr.x, sqr.y)
            t.pendown()
            for n in range(5):
                t.begin_fill()
                t.forward(sqr.size)
                t.right(90)
                t.end_fill()
            screen.clear()
        turtle.done()
