#!/usr/bin/python3
""" module for addition function: the add_ineger method """


def add_integer(a, b=98):
    """ method that adds 2 integers.

    args:
        a: the first integer.
        b: the second integer, default 98.

    Raises:
        TypeError or exception: If a or b are not integers, float.

    Returns:
        The sum of the two integers
    """

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
