#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """i
    Replace all occurrence of an element with another

    Args:
    my_list: a list of elements
    search: the element to replace in the list
    replace: the new element
    """

    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace

    return new_list
