#!/usr/bin/python3
""" Module for BaseGeometry class"""


class BaseGeometry:
    """ class BaseGeometry"""
    def area(self):
        """method that raises an Exception with the message:
        area() is not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """method that validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
