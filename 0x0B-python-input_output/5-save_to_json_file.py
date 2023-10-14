#!/usr/bin/python3
""" Module for save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    json_string = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json_string)
