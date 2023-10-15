#!/usr/bin/python3
""" Module for class Student"""


class Student:
    """ class that defines Student"""
    def __init__(self, first_name, last_name, age):
        """" instantiation of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            """return {attr: getattr(self, attr)
            for attr in attrs if hasattr(self, attr)}"""
            json_dic = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dic[attr] = getattr(self, attr)
            return json_dic

    def reload_from_json(self, json):
        """method that replaces all attributes of the Student instance"""
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
