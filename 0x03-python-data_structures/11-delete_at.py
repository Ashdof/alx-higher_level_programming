#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Delete an element at a specific position

    my_list: a list of elements
    idx: the position to delement the element
    """

    if idx >= 0 and idx < len(my_list):
        del my_list[idx]

    return (my_list)
