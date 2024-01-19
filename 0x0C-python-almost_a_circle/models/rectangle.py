#!/usr/bin/python3
""" Module for Rectangle class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """ Representes a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ The constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """set & get the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set & get the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set & get the value of x  of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set & get the value of y of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """public method:
        returns the area value of the Rectangle i,stance
        """
        return self.__height * self.__width

    def display(self):
        """public method:
        prints in stdout the Rectangle instance
        """
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """ returns a str representation of the instance
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[{self.__class__.__name__}] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def display(self):
        """public method:
        print in stdout the Rectangle instance with the character #
        by taking care of x and y
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """ public method:
        assigns an argument to each attribute or key/value
        """
        if len(args) >= 1:
            self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            keys = list(kwargs.keys())
            if (keys.count("id") == 1):
                self.id = kwargs["id"]
            if (keys.count("height") == 1):
                self.__height = kwargs["height"]
            if (keys.count("width") == 1):
                self.__width = kwargs["width"]
            if (keys.count("x") == 1):
                self.__x = kwargs["x"]
            if (keys.count("y") == 1):
                self.__y = kwargs["y"]
