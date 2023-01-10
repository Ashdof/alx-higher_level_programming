#!/usr/bin/python3
"""File Operation"""


def write_file(filename="", text=""):
    """Write to File

    Description:
        This function writes a string to a text file. It creates the
        file if it doesn't already exits; if it exists, it wipes its
        contents

    Args:
        filename (str): the name of the file
        text (str): the string to write to the file
    """
    with open(filename, 'w', encoding='UTF-8') as wf:
        return wf.write(text)
