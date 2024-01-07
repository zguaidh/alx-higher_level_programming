#!/usr/bin/python3
"""
Module for matrix_divided method
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix:

    Args:
        matrix: must be a list of lists of integers or floats
        div: must be a number (integer or float)

    Raises:
        - TypeError:
        if the matrix is not int of float
        or
        if the rows of the matrix arnt the same size
        or
        if div is not int or float
        - ZeroDivisionError:         if div is equal to zero
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError('matrix must be a matrix '
                        '(list of lists) of integers/floats')
    else:
        for ls in matrix:
            if not isinstance(ls, list):
                raise TypeError('matrix must be a matrix '
                                '(list of lists) of integers/floats')
            else:
                for elem in ls:
                    if type(elem) not in (int, float):
                        raise TypeError('matrix must be a matrix '
                                        '(list of lists) of integers/floats')
    if len(matrix) != 0:
        for row in range(len(matrix) - 1):
            if len(matrix[row]) != len(matrix[row + 1]):
                raise TypeError('Each row of the '
                                'matrix must have the same size')

    if type(div) not in (int, float):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    m = [ls[:] for ls in matrix]
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = round((m[i][j] / div), 2)
    return m


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/2-matrix_divided.txt')
