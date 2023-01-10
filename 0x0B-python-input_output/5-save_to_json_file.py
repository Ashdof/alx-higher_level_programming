#!/usr/bin/python3
"""File Input/Output Operations"""

import json


def save_to_json_file(my_obj, filename):
    """Save to JSON File

    Description:
        This function writes an Object to a text file,
        using a JSON representation

    Args:
        my_obj (object): the object to write to the file
        filename (str): the name of the file
    """
    with open(filename, 'w', encoding='UTF-8') as wo:
        wo.write(json.dumps(my_obj))
