#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replace an element of a list at a specific position

    my_list: a list of elements
    idx: the position to replace an element
    element: the element to replace at the given position
    """

    if idx < 0 or idx > len(my_list):
        return my_list

    for i in range(len(my_list)):
        if i == idx:
            my_list[i] = element

    return my_list
