#!/usr/bin/python3
"""A matrix definition function"""


def matrix_divided(matrix, div):
    """Matrix division

    Description:
        This function divides a given matrix by an integer value. The matrix
        is a list of lists of integers or floats

    Args:
        matrix (int/floats): the first argument
        div (int/float) the second argument

    Returns:
        A matrix of the divided values
    """

    type_msg = "matrix must be a matrix (list of lists) of integers/floats"
    size_msg = "Each row of the matrix must have the same size"
    div_zero = "division by zero"
    div_type = "div must be a number"

    if type(div) not in (int, float):
        raise TypeError(div_type)

    if div == 0:
        raise ZeroDivisionError(div_zero)

    if not matrix or not isinstance(matrix, list):
        raise TypeError(type_msg)

    size = 0
    for row in matrix:
        if size != 0 and len(row) != size:
            raise TypeError(size_msg)

        size = len(row)

        if type(row) not in (list, ):
            raise TypeError(type_msg)

        for item in row:
            if type(item) not in (int, float):
                raise TypeError(type_msg)

    ans = list(map(lambda x: list(map(lambda y: round(y/div, 2), x)), matrix))
    return ans
