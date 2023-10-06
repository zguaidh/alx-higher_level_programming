#!/usr/bin/python3
""" module for a function that prints a square with the character #
    - size is the size length of the square and it must be an integer, otherwise raise an exception
    - if size is less than 0, raise an exception 
    - if size is a float and is less than 0, raise an exception
    """


def print_square(size):
    """ method that prints a square with the character #.
        - size: is the size length of the square
        - Raises: an exception if size is less than 0 or size is a float and is less than 0 """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
