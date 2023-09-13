#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = my_list[:]
    idx = copy.index(search)
    copy.pop(idx)
    copy.insert(idx, replace)
    for i in range(len(copy)):
        while copy[i] == search:
            search_replace(copy, search, replace)
            i += 1
    return copy
