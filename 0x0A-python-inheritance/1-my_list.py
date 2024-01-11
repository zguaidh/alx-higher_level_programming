#!/usr/bin/python3
"""Module for class MyList"""


class MyList(list):
    """ class that inherits from list"""
    def print_sorted(self):
        """ prints the sorted list"""
        ls = self.copy()
        ls.sort()
        print(ls)
