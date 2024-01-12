#!/usr/bin/python3
"""Module for MyInt class"""


class MyInt(int):
    """class MyInt that inherits from int"""
    def __eq__(self, other):
        """defines behavior of the == operator"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """defines behavior of the != operator"""
        return int.__eq__(self, other)
