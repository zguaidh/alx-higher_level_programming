#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ls = []
    for key in a_dictionary:
        ls.append(key)
    ls.sort()
    for i in range(len(ls)):
        print(ls[i]+": "+str(a_dictionary[ls[i]]))
