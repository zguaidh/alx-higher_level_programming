#!/usr/bin/python3
"""module for a function that multiplies 2 matrices by using the module NumPy
    - Test cases should be the same as 100-matrix_mul
    but with new exception type/message
    """


def lazy_matrix_mul(m_a, m_b):
    """method that multiplies 2 matrices by using the module NumPy
    -m_a: the first matrix
    -m_a: the second matrix """
    if not isinstance(m_a, list):
        raise TypeError("

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
