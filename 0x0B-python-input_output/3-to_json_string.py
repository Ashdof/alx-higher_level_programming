#!/usr/bin/python3
"""Serialize an object"""

import json


def to_json_string(my_obj):
    """
    Serialize an object

    Args:
        my_obj (obj): the object to serialize

    Returns:
        The serialized object
    """

    return json.dumps(my_obj)
