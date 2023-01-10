#!/usr/bin/python3
"""File Input/Output Manipulation"""

import json


def to_json_string(my_obj):
    """To JSON

    Description:
        This file returns the JSON representation of an object

    Args:
        The object
    """
    return json.dumps(my_obj)
