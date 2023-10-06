#!/usr/bin/python3
"""module for a function that prints a text with 2 new lines after each of these characters: ., ? and :
    - text must be a string, otherwise raise a TypeError exception with the message text must be a string
    - There should be no space at the beginning or at the end of each printed line
    """


def text_indentation(text):
    """ method that prints a text with 2 new lines after each of these characters: ., ? and :
        - text: the string to indent
        - Raise: an exceprion when text is not a string"""


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
