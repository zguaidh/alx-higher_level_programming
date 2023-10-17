#!/usr/bin/python3
"""Module for Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class that inherits from the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """ The constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """inform the user about the information of the square"""
        return "[{}] ({}) {}/{} - {}".\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ The getter for size(width) of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """The size setter"""
        self.width = value
        self.height = value

    def update_0(self, id=None, size=None, x=None, y=None):
        """method that updates instance attributes throught args or kwargs"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """checks if mwargs or arguments - no-keyworded arguments"""
        if args:
            self.update_0(*args)
        elif kwargs:
            self.update_0(**kwargs)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
