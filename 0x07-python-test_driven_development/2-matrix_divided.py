#!/usr/bin/python3
"""A module with a matrix definition function"""


def matrix_divided(matrix, div):
    """
    Matrix division

    Args:
        matrix (int/float): a matrix of integers or floats or both
        div (int/float): the value to divide the matrix

    Return:
        A matrix of divided values
    """

    err_type = "matrix must be a matrix (list of lists) of integers/floats"
    err_size = "Each row of the matrix must have the same size"
    err_zero = "division by zero"
    err_div_type = "div must be a number"

    size = 0

    if type(div) not in (int, float):
        raise TypeError(err_div_type)

    if div == 0:
        raise ZeroDivisionError(err_zero)

    if not matrix or not isinstance(matrix, list):
        raise typeError(err_type)

    for row in matrix:
        if size != 0 and len(row) != size:
            raise TypeError(err_size)

        size = len(row)

        if type(row) not in (list, ):
            raise TypeError(err_type)

        for item in row:
            if type(item) not in (int, float):
                raise TypeError(err_type)
    ans = list(map(lambda x: list(map(lambda y: round(y/div, 2), x)), matrix))

    return ans
