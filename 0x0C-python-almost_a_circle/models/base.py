#!/usr/bin/python3
"""Module for the Base class"""
import json


class Base:
    """The class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ The constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) ==0:
            return "[]"
        else:
            json_str = json.dumps(list_dictionaries)
            return json_str
