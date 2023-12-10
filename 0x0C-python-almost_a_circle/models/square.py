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

    def __str__(self):
        """Override Rects str representation"""
        p = f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y} - {self.width}"
        return p
