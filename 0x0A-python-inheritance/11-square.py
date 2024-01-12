#!/usr/bin/python3
"""Module for class Square"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size):
        """The constructor"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Computes the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Return a string represantation of the square"""
        return f"[{__class__.__name__} {self.__size}/{self.__size}]"
