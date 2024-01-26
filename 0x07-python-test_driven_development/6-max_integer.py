#!/usr/bin/python3
"""A module with a function to find the max integer in a list"""


def max_integer(list=[]):
    """Find the maximum integer of a list"""

    if len(list) == 0:
        return None

    max_value = list[0]
    for i in list:
        if i > max_value:
            max_value = i
    return max_value
