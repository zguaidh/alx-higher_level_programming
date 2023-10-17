#!/usr/bin/python3
"""Module for a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The getter for the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """the setter of the width"""
        self.int_validation("width", value, False)
        self.__width = value

    @property
    def height(self):
        """the getter for the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter of the height"""
        self.int_validation("height", value, False)
        self.__height = value

    @property
    def x(self):
        """The getter for x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """The setter of x"""
        self.int_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """The getter for y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """The setter for y of the rectangle"""
        self.int_validation("y", value)
        self.__y = value

    def int_validation(self, name, value, eql=True):
        """method for value validation"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eql and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eql and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """method to compute the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """method that prints the rectangle to stdout using #"""
        dis = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(dis, end="")

    def __str__(self):
        """overrides the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.x, self.y, self.width, self.height)
