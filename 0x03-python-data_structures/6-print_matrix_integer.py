#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for elem in matrix:
        for i in elem:
            if i != elem[-1]:
                print("{:d}".format(i), end=" ")
            else:
                print("{:d}".format(i), end="")
        print()
