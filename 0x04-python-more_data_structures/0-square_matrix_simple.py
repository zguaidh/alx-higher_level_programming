#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr = []
    for i in range(len(matrix)):
        sqr += [list(map(lambda x: x ** 2, matrix[i]))]
    return sqr
