#!/usr/bin/python3
"""Function to check the instance of an object"""


def is_same_class(obj, a_class):
    """Check instance of a class

    Description:
        This function checks if an object is the exact instance
        of a given class

    Args:
        obj (object of a class): the object parameter
        a_class (class): the class parameter

    Returns:
        True if obj is an instance of a_class
        False otherwise

    """

    if type(obj) == a_class:
        return True
    else:
        return False
