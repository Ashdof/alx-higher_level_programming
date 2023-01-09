#!/usr/bin/python3
"""Define an object lookup function"""


def lookup(obj):
    """Lookup attributes

    Description:
        This function looks up and returns a list of attributes
        and methods of an obejct defined by its parameter

    Args:
        obj (object): the object parameter

    Returns:
        A list of attributes and methods of the object
    """

    return dir(obj)
