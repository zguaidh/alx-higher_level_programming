#!/usr/bin/python3
"""module for a function that prints My name is <first name> <last name>
    - first_name and last_name must be strings
    otherwise, raise a TypeError exception with the message:
    first_name must be a string or last_name must be a string
    """


def say_my_name(first_name, last_name=""):
    """ method that prints My name is <first name> <last name>
    - first_name: is the first name
    - last_name: is the last name, or default an empty string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
