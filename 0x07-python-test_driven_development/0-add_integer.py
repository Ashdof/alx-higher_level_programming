#!/usr/bin/python3
"""A module with function that adds two integers"""


def add_integer(a, b=98):
    """
    Add two integer values

    Args:
        a (int): the first integer
        b (int): the second integer with default value of 98

    Return:
        The integer sum of the two args
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
