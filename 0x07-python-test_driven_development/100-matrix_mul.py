#!/usr/bin/python3
""" module for a function  that multiplies 2 matrices:
    - m_a and m_b must be validated with these requirements in this order
    - m_a and m_b must be an list of lists of integers or floats
    - If m_a and m_b can’t be multiplied: raise a ValueError exception 
    """


def matrix_mul(m_a, m_b):
    """ method that multuplies 2 matrices
        - m_a: the first matrix
        - m_a: the second matrix
    """



if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")

