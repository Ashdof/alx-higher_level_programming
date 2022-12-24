#!/usr/bin/python3
"""Addition of two numbers"""


def add_integer(a, b=98):

    """Add two numbers

    Description:
        This function adds the values of its parameters

    Arguments:
        a (int/float): the first parameter. A value of type integer
        or float

        b (int/float): the second parameter. A value of type integer
        or float

    Return:
        an integer; the sum of a and b
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
