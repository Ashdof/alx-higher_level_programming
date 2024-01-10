#!/usr/bin/python3

def number_keys(a_dictionary):
    """
    Compute number of keys

    Args:
    a_dictionary: the dictionary of items

    Return: number of keys
    """
    keys = []

    for k, v in a_dictionary.items():
        keys.append(k)

    return len(keys)
