#!/usr/bin/python3
""" Module for the write_file method"""


def write_file(filename="", text=""):
    """ method that zrites a string to a text file
        args:
            filename: the file to write in
            text: the text to write to the file
        return:
           the number of characters written
    """
    count = 0
    with open(filename, "w", encoding="utf-8") as file:
        for i in range(len(text)):
            file.write(text[i])
            count += 1
    return count
