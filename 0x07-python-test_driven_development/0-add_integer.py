#!/usr/bin/python3
""" module for addition function: the add_ineger method 
    - a and b must be integers or floats, otherwise raise a TypeError
    - a and b must be first casted to integers if they are float
    - Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """ method that adds 2 integers.
        a: the first integer.
        b: the second integer, default 98."""

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
