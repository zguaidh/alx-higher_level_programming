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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        pass

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string"""
        ls = []
        if json_string is None or not json_string:
            return ls
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls.__name == "Square":
            dummy = cls(1)
            dummy.update(**dictionary)
            return dummy
        elif cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy
