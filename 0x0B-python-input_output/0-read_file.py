#!/usr/bin/python3
""" Module for a read_file method"""


def read_file(filename=""):
    """ method that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()
        print(contents, end="")
