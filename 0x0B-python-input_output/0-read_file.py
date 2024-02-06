#!/usr/bin/python3
"""A function that reads a text file"""


def read_file(filename=""):
    """Read file

    Args:
        filename (str): the name or path to the file
    """

    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
