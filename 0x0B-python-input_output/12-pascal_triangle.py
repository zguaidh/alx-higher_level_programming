#!/usr/bin/python3
""" module for the pascal_triangle"""


def pascal_triangle(n):
    """" returns a list of lists of integers representing:
    the Pascal’s triangle of n"""
    ls = []
    i = 1
    if n <= 0:
        return ls
    else:
        triangle = [[1]]
        while len(triangle) != n:
            elem = triangle[-1]
            last_elem = [1]
            for i in range(len(elem) - 1):
                last_elem.append(elem[i] + elem[i + 1])
            last_elem.append(1)
            triangle.append(last_elem)
        return triangle
