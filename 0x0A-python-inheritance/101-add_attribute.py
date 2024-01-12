#!/usr/bin/python3
"""Module for add_attribute method"""


def add_attribute(obj, attr, value):
    """adds a new attribute to an object if it’s possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
