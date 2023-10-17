#!/usr/bin/python3
""" Module for a Base class"""


import json


class Base:
    """ A representation of the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The constructor: instantiation of the class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
