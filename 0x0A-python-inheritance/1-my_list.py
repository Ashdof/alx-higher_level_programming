#!/usr/bin/python3
""" Define a inheriting function """


class MyList(list):
    """Inherit from list

    Description:
        This class inherits from the built-in list class

    Args:
        list (list): the built-in list class
    """

    def __init__(self):
        """Initialise the class"""
        super().__init__()

    def print_sorted(self):
        """Print a list in ascending order"""
        print(sorted(self))
