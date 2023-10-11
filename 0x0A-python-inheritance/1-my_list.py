#!/usr/bin/python3
"""Module for a class Mylist"""


class MyList(list):
    """Class that inherits from list"""

    
    def print_sorted(self):
        """Public instance method:
            prints the list, but sorted (ascending sort)
        """
        print(sorted(self))

