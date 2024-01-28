#!/usr/bin/python3
"""A module with a function that multiplies two matrices"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices

    Description:
        This function multiplies two natrices passed via arguments

    Args:
        m_a (list of list): the first parameter of integers or floats
        m_b (list of list): the second parameter of integers or floats

    Raises:
        TypeError exception for invalid types
        ValueError exception for invalid values
    """
    if type(m_a) not in (list, ):
        raise TypeError("m_a must be a list")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if type(m_b) not in (list, ):
        raise TypeError("m_b must be a list")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    size_a, size_b = 0, 0

    for row_a in m_a:
        if size_a != 0 and len(row_a) != size_a:
            raise TypeError("each row of m_a must be of the same size")

        size_a = len(row_a)

        if type(row_a) not in (list, ):
            raise TypeError("m_a must be a list of lists")

        for item in row_a:
            if type(item) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for row_b in m_b:
        if size_b != 0 and len(row_b) != size_b:
            raise TypeError("each row of m_b must be of the same size")

        size_b = len(row_b)

        if type(row_b) not in (list, ):
            raise TypeError("m_b must be a list of lists")

        for item in row_b:
            if type(item) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
