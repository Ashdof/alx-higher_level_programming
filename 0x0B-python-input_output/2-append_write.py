#!/usr/bin/python3
"""Append to a text file"""


def append_write(filename="", text=""):
    """
    Append to a text file

    Description:
        This function adds data to the end of the contents
        of a text file

    Args:
        filename (str): the name or the path to the file
        text (str): the data to write to the file

    Return:
        Number of characters written to the file
    """

    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
