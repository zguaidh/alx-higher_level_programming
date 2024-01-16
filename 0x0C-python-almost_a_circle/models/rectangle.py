#!/usr/bin/python3
""" Module for Rectangle class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """ Representes a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ The constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """set & get the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """set & get the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """set & get the value of x  of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """set & get the value of y of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
