#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Find the biggest integer of a list

    my_list: a list of integers
    """
    if len(my_list) == 0:
        return None
    n = my_list[0]

    for i in my_list:
        if i > n:
            n = i

    return n
