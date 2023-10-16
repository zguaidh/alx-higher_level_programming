#!/usr/bin/python3
""" Module for append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file,
    after each line containing a specific string"""
    with open(filename, "r", encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, "w", encoding='utf-8') as file:
        for line in lines:
            file.write(line)

            if search_string in line:
                file.write(new_string)
