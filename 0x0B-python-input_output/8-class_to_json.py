#!/usr/bin/python3
"""Define a Python class-to-JSON function"""


def class_to_json(obj):
    """
    Dictionary description of an object

    Description:
            This function returns a dictionary description with a simple data
            structure for a JSON serialisation of an object

    Args:
        obj (object): the given object

    Returns:
        A dictionary represntation of a simple data structure
    """

    return obj.__dict__
