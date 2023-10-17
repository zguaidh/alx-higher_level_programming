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
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)
