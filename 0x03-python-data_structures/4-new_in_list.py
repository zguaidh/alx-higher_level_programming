#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0:
        return my_list
    elif idx >= length:
        return my_list
    else:
        new_list = my_list[:]
        del new_list[idx]
        new_list.insert(idx, element)
        return new_list
