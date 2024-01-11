#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Delete a key from the dictionary object

    Args:
    a_dictionary: the dictionary object
    key: the key to delete

    Return: the dictionary object
    """
    if key == "" or key not in a_dictionary.keys():
        return a_dictionary

    del a_dictionary[key]
    return a_dictionary
