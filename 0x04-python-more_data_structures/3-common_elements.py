#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Return a set of common elements in two sets

    set_1: the first set of elements
    set_2: the second set of elements

    Return: a set of common elements
    """
    return [i for i in set_1 for j in set_2 if i == j]
