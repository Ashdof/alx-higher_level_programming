#!/usr/bin/python3
"""A module with a function that prints a square"""


def print_square(size):
    """
    Print a square with the '#' character

    Args:
        size (int/float): the size of the square
    """

    err_type = "size must be an integer"
    err_zero = "size must be >= 0"

    if not isinstance(size, int):
        raise TypeError(err_type)
    elif size < 0 and isinstance(size, float):
        raise TypeError(err_type)

    if size < 0:
        raise ValueError(err_zero)

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
