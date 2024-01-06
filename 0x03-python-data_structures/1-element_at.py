#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Retrieve an element from a list

    my_list: a list of elements
    idx: an integer value
    """

    if idx < 0 or idx > len(my_list):
        return None
    else:
        for i in range(len(my_list)):
            if i == idx:
                return my_list[i]
