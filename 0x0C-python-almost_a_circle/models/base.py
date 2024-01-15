#!/usr/bin/python3
"""Module for the Base class"""


class Base:
    """The class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ The constructor"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
