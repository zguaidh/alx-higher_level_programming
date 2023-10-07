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
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    m_a_emp = False
    m_b_emp = False
    m_a_norect = False
    m_b_norect = False
    m_a_notnum = False
    m_b_notnum = False
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            m_a_norect = True
        for i in row:
            if not isinstance(i, (int, float)):
                m_a_notnum = True

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            m_b_notnum = True
        for i in row:
            if not isinstance(i, (int, float)):
                m_b_notnum = True

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be emty")

    if m_a_notnum:
        raise TypeError("m_a should contain only integers or floats")
    if m_b_notnum:
        raise TypeError("m_b should contain only integers or floats")
    if m_a_norect:
        raise TypeError("each row of m_a must be of the same size")
    if m_b_norect:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = [[] for i in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            x = 0
            for k in range(len(m_b)):
                x += m_a[i][k] * m_b[k][j]
            result[i].append(x)

    return result


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
