#!/usr/bin/python3
"""Determine the instance of an object"""


def inherits_from(obj, a_class):
    """Instance of a class

    Description:
        This function determines whether an onject is an instance of
        a class that inherited (directly or indirectly) from the
        specified class

    Args:
        obj (object): the object parameter
        a_class (class): the class parameter

    Returns:
        True if obj is an instance of a class that inherited
        (directly or indirectly) from the specified class or
        False otherwise
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True

    return False
