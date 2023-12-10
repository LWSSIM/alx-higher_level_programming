#!/usr/bin/puthon3
"""Square class inherit from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """

    Note:
        this class has no class attributes
        Parent takes care of validation and assignment

    Methods:
        __init__: init the class attributes
        __str__:
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initialise a new square based on REctangle
        __init__
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.integer_validator("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update Rectangle attribues"""
        attr = ["id", "size", "x", "y"]
        x = 0
        if len(args):
            for i in args:
                setattr(self, attr[x], i)
                x += 1
        elif len(kwargs):
            for i, j in kwargs.items():
                setattr(self, i, j)

    def __str__(self):
        """Override Rects str representation"""
        p = (
            f"[{type(self).__name__}] "
            f"({self.id}) "
            f"{self.x}/{self.y} "
            f"- {self.size}"
        )
        return p
