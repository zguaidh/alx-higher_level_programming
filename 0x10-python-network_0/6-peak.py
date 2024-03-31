#!/usr/bin/python3
"""task 6 modele"""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None
    else:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
