#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """i
    Replace all occurrence of an element with another

    Args:
    my_list: a list of elements
    search: the element to replace in the list
    replace: the new element
    """

    new_list = [list(map(lambda x: replace if x == search else x, my_list))]
    return new_list
