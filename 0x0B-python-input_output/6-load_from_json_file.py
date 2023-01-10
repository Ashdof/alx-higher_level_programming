#!/usr/bin/python3
"""File Input/Output Operations"""

import json


def load_from_json_file(filename):
    """Create object

    Description:
        This function creates an object froma json file

    Args:
        filename (json): the name of the json file

    Return:
        An object
    """
    with open(filename) as ljs:
        return json.load(ljs)
