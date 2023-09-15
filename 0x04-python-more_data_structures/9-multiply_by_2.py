#!/usr/bin/python3
def val_mul(x):
    return x * 2


def multiply_by_2(a_dictionary):
    for key, value in a_dictionary.items():
        a_dictionary[key] = val_mul(value)
    return a_dictionary
