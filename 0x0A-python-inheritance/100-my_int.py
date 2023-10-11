#!/usr/bin/python3
"""
Contains the class MyInt
"""


class MyInt(int):
    """
    A rebel class that modifies the behaviour of == and !=
    """
    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super().__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """override the == operator to check for inequality"""
        return int(self) != other

    def __ne__(self, other):
        """override the != operator to check for equality"""
        return int(self) == other
