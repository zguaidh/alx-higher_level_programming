#!/usr/bin/python3
def val_mul(x):
    return x * 2


def multiply_by_2(a_dictionary):
    dic = dict(a_dictionary)
    for key, value in dic.items():
        dic[key] = val_mul(value)
    return dic
