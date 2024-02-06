#!/usr/bin/python3
"""Deserialize a JSON file"""

import json


def from_json_string(my_str):
    """
    Deserialize a JSON file

    Args:
        my_str (json): the data to deserialize

    Returns:
        The deserialized object
    """

    return json.loads(my_str)
