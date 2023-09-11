#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return
    ls = []
    for char in my_string:
        ls.append(char)
    for elem in ls:
        if elem == 'c' or elem == 'C':
            ls.remove(elem)
    ls = [char for char in ls if char not in ['c', 'C']]
    STR = ''.join(ls)
    return STR
