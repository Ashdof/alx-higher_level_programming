#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Update a dictionary

    Args:
    a_dictionary: the dictionary object with elements
    key: a key in the a_dictionary
    value: the value to store in the dictionary

    Return: the dictionary object
    """
    a_dictionary[key] = value
    return a_dictionary
