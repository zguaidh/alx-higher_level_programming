#!/usr/bin/python3
""" Modul of a method that divides all elements of a matrix
    - matrix must be a list of lists of integers or floats, otherwise raise a TypeError
    - Each row of the matrix must be of the same size, otherwise raise a TypeError
    - div can't be equal to 0 and  must be integer or float, otherwise raise an exception
    - All elements of the matrix should be divided by div, rounded to 2 decimal places """

def matrix_divided(matrix, div):
    """ method that devides all eleme,ts of a matrix:
        - matrix: the matrix to be divided
        - div: the number the matrix should be divided by"""
    div_matrix = []

    if not(isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in (matrix):
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    for elem in matrix:
        for i in elem:
            if not(isinstance(i, int) or isinstance(i, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        div_row = []
        for elem in row:
            div_row.append(round(elem / div, 2))
        div_matrix.append(div_row)
    return div_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
