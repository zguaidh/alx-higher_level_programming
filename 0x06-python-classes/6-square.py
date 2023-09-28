#!/usr/bin/python3
"""Square module"""


class Square:
    """defines a square by its size"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__position = position
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
    """method that retreives the position attribute"""
    @property
    def position(self):
        return self.__position
    """method to set the position attribure"""
    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    """method that prints in stdout the square with the character #"""
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            if self.__position[1] > 0:
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print(i)
