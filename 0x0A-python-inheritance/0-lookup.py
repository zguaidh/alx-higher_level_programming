#!/usr/bin/python3
""" Module for lookup method. """


def lookup(obj):
    """Returns the list of available attributes and methods of an object:
        Args:
            obj: The object to list

        Returns:
            list: the list of attributes and methods
    """
    return dir(obj)
