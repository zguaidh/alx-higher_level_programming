#!/usr/bin/python3
""" Module for Rectangle class that inherits from Base"""
From models.Base import Base


class Resctangle(Base):
    """ Representes a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ The constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
