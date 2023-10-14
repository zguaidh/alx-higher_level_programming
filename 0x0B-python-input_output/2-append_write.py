#!/usr/bin/python3
""" Module for the append_write function"""
def append_write(filename="", text=""):
    """method that appends a string at the end of a text file
        Args:
            filename: the file to a write to
            text: the string to append
        Return:
            the number of characters added
    """
    count = 0
    with open(filename, "a", encoding="utf-8") as file:
        for i in range(len(text)):
            file.write(text[i])
            count += 1
    return count
