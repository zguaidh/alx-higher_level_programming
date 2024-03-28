#!/usr/bin/python3
"""task 6 modele"""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)
    else:
        list_of_integers.sort()
        return list_of_integers[size - 1]
