#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Obtain a set of unique elemenets

    Args:
    set_1: the first set of elements
    set_2: the second set of elements

    Return: a set of unique elements
    """
    return (set_1 ^ set_2)
