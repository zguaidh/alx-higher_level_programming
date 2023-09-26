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
    """ method to retreive the size attribute"""
    @property
    def size(self):
        return self.__size
    """method to set the size attribute"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """method that prints in stdout the square with the character #"""
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
