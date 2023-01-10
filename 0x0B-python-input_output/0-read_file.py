#!/usr/bin/python3
"""Read from File"""


def read_file(filename=""):
    """Read file

    Description:
        This function reads from a file prints the content to the
        stdout

    Args:
        filename (str): the name of the file to read from
    """
    with open(filename, 'r', encoding='UTF-8') as rf:
        for line in rf:
            print(line)
