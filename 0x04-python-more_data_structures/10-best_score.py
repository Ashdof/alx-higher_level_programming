#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Obtain key with biggest integer value

    Args:
    a_dictionary: the dictionary object

    Return: key with biggest values
    """
    if a_dictionary is None:
        return None

    return max(a_dictionary, key=a_dictionary.get)
