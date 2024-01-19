#!/usr/bin/python3
"""Module for Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """The constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ The str representation of the square"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} \
- {self.width}"

    @property
    def size(self):
        """get/set the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if args:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            keys = list(kwargs.keys())
            if (keys.count("id") == 1):
                self.id = kwargs["id"]
            if (keys.count("size") == 1):
                self.size = kwargs["size"]
            if (keys.count("x") == 1):
                self.x = kwargs["x"]
            if (keys.count("y") == 1):
                self.y = kwargs["y"]
