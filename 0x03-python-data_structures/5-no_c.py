#!/usr/bin/python3
def no_c(my_string):
    ls = []
    for char in my_string:
        ls.append(char)
    for elem in ls:
        if elem == 'c' or elem == 'C':
            ls.remove(elem)
    STR = ''.join(ls)
    return STR