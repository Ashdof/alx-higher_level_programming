#!/usr/bin/python3
"""A function that writes to a text file"""


def write_file(filename="", text=""):
    """
    Write to File

    Description:
        This function writes toa text file

    Args:
        filename (str): the name or the path to the file
        text (str): the data to write to the file

     Returns:
        Number of characters written to the file
    """

    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
