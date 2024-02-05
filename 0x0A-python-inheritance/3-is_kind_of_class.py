#!/usr/bin/python3
"""Check whether an object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """Instance of a class

    Description:
        This function determines whether an onject is an instance of
        a class or an instance of a class that inherist from the
        specified class

    Args:
        obj (object of a class): the object parameter
        a_class (class): the class parameter

    Returns:
        True if obj is an instance of a_class or False otherwise

    """

    if isinstance(obj, a_class) or type(obj) == a_class:
        return True

    return False
