#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replace an element of a list at a given position

    my_list: a list of elements
    idx: the position to replace an element
    element: the new element to replace an old one
    """

    cpy = my_list.copy()

    if idx < 0 or idx > len(my_list):
        return cpy

    cpy[idx] = element
    return cpy
