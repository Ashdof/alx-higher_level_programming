#!/usr/bin/python3
"""Deserialize a JSON string"""

import json


def load_from_json_file(filename):
    """
    Deserialize a JSON string

    Description:
        This function creates an object from
        a JSON file

    Args:
        filename (json): the name or the path to the file
    """

    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
