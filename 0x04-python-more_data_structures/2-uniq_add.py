#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_list = set(my_list)
    liste = list(set_list)
    result = 0
    for i in range(len(liste)):
        result = result + liste[i]
    return result
