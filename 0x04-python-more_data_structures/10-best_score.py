#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Obtain key with biggest integer value

    Args:
    a_dictionary: the dictionary object

    Return: key with biggest values
    """
    max_value = 0

    if a_dictionary is None:
        return None

    for value in a_dictionary.values():
        if value > max_value:
            max_value = value

    for key in a_dictionary.keys():
        if a_dictionary[key] == max_value:
            max_key = key

    return max_key
