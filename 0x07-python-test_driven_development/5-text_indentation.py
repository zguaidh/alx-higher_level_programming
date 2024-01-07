#!/usr/bin/python3
"""
Module for text_indentation function
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after these chars: ., ? and :

    Args:
        text: must be str text.

    Raises:
        TypeError: If text is not a str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
