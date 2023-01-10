#!/usr/bin/python3
"""File Input/Output Operations"""


def append_write(filename="", text=""):
    """Append to a File

    Description:
        This function appends a string at the end of a text file

    Args:
        filename (str): the name of the file
        text (str): the string to append to the file

    Returns:
        The number of characters added
    """
    with open(filename, 'a', encoding='UTF-8') as ap:
        return ap.write(text)
