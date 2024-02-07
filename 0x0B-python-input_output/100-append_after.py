#!/usr/bin/python3
"""Append to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Append to a file

    Description:
        This function inserts a line of text to a file, after each
        line containing a specific string

    Args:
        filename (str): the name of the file
        search_string (str): the string to search for and append a new string
        after it
        new_string (str): the new string to append to the text file
    """

    line = ""
    with open(filename) as f:
        for val in f:
            line += val
            if search_string in val:
                line += new_string

    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(line)
