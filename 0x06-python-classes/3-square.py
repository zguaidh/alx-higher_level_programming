#!/usr/bin/python3
"""Square module"""


class Square:
    """defines a square by its size"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    """ method that returns the current square area"""
    def area(self):
        return self.__size ** 2
