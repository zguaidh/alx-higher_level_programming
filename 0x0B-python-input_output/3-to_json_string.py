#!/usr/bin/python3
import json
"""Module for to_json_string function"""


def to_json_string(my_obj):
    """ method that  returns the JSON representation of an object (string)"""
    json_string = json.dumps(my_obj)
    return json_string
