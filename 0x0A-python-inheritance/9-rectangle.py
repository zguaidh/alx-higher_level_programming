#!/usr/bin/python3
""" Module for Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """
        The constructor
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Computes the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return a str represantation of the class"""
        return f"[{__class__.__name__}] {self.__width}/{self.__height}"
