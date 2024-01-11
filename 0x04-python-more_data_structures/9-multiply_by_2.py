#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    Update keys of a dicionary by multiplying each by 2

    Args:
    a_dictionary: the dictionary object

    Return: a new dictionary
    """
    new_dict = {}

    for k, v in a_dictionary.items():
        new_dict[k] = 2 * v

    return new_dict
