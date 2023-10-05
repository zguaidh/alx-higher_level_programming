#!/usr/bin/python3
"""
module for a class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    Defines a  Rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Init the rectangle """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for the private instance attribute: width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter for the Private instance attribute: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for the Private instance attribute: height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method that returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """method that returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns the rectangle with the character #"""
        ret_str = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height - 1):
                ret_str += str(self.print_symbol) * self.__width
                ret_str += "\n"
            ret_str += str(self.print_symbol) * self.__width
        return ret_str

    def __repr__(self):
        """ returns a string representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance with width == height == size"""
        return cls(size, size) 
