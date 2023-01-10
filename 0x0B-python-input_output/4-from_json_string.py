#!/usr/bin/python3
"""File Input/Output Manipulation"""

import json


def from_json_string(my_str):
    """Decode JSON object

    Description:
        This function decodes a JSON object to a Python object

    Args:
        my_str (json string): the JSON string

    Returns:
        A Python representation of the JSON string
    """
    return json.loads(my_str)
