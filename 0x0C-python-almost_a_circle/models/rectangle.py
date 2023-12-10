#!/usr/bin/python3
"""rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base

    Note:
        uses id from base

    Attr: (all int)
        width
        height
        x
        y

    Methods:
        __init__: init the class attributes
    """

    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        """init method

        Args:
            width (dimensions)
            height

            x (position)
            y

            id
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.integer_validator("y", value)
        self.__y = value

    def area(self):
        """public method to calculate area

        Return:
            area int
        """
        return self.width * self.height

    def display(self):
        """display an instance using a character"""
        w = self.width
        h = self.height
        x = self.x
        y = self.y

        if y > 0:
            print(("\n" * y), end="")

        print((((" " * x) if x > 0 else "") + ("#" * w) + "\n") * h, end="")

    def update(self, *args, **kwargs):
        """update Rectangle attribues"""
        attr = ["id", "width", "height", "x", "y"]
        x = 0
        if len(args):
            for i in args:
                setattr(self, attr[x], i)
                x += 1
        elif len(kwargs):
            for i, j in kwargs.items():
                setattr(self, i, j)

    def __str__(self):
        """over-riden str method"""
        id = self.id
        n = type(self).__name__
        w = self.width
        h = self.height
        x = self.x
        y = self.y

        p = f"[{n}] ({id}) {x}/{y} - {w}/{h}"
        return p
