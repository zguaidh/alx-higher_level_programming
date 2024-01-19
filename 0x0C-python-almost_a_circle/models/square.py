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
