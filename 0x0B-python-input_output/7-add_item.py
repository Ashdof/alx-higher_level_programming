#!/usr/bin/python3
"""
Append arguments to a list

Description:
    These program adds all arguments to a list and saves
    the list in a JSON file
"""

import sys


if __name__ == "__main__":
    load = __import__("6-load_from_json_file").load_from_json_file
    save = __import__("5-save_to_json_file").save_to_json_file

    try:
        vals = load("add_item.json")
    except FileNotFoundError:
        vals = []

    vals.extend(sys.argv[1:])
    save(vals, "add_item.json")
