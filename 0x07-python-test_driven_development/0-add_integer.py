#!/usr/bin/python3
"""
0-add_integer module
"""


def add_integer(a, b=98):
    """
    Function that adds two integers

    args:
        a: first arg must be integer or float
        b: Second arg must be integer or foat

    Raises:
        TypeError: whene one of the args is not integer or float

    Returns:
        an integer: the addition od a and b
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError('a must be an integer')
    if not isinstance(b, int):
        raise TypeError('b must be an integer')
    else:
        return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
