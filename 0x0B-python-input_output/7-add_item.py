#!/usr/bin/python3
"""File Input/Output Operations

Description:
    This function adds all arguments to a Python list, and then save
    them to a file. It firsts imports the load_from_json_file() to load
    the json file assign it to the variable load_json. It also imports
    the save_to_json_file() function and assigns it to the variable
    save_json.

    It then adds all arguments passed to the program to a list and then
    saves them to a file using the save_json variable.

    If the file does not exists, it saves an empty list
"""

import sys


if __name__ == '__main__':
    load_json = __import__('6-load_from_json_file').load_from_json_file
    save_json = __import__('5-save_to_json_file').save_to_json_file

    try:
        vals = load_json("add_item.json")
    except FileNotFoundError:
        vals = []

    vals.extend(sys.argv[1:])
    save_json(vals, "add_item.json")
