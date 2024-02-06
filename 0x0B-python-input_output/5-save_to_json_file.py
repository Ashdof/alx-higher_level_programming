#!/usr/bin/python3
"""Write object to file"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write to file

    Description:
        This function serializes an object and writes the
        it to a text file

    Args:
        my_obj (obj): the object to serialize
        filename (str): the name or the path to the file
    """

    with open(filename, "w", encoding="UTF-8") as f:
        f.write(json.dumps(my_obj))
