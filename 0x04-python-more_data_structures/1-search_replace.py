#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search not in my_list:
        return my_list
    copy = my_list[:]
    while search in copy:
        idx = copy.index(search)
        copy.pop(idx)
        copy.insert(idx, replace)
    return copy
