#!/usr/bin/python3
"""A class that inherits from the built-in list"""


class MyList(list):
    """A class that inherits from the built-in list"""

    def __init__(self):
        """Initialize object"""

        super().__init__()

    def print_sorted(self):
        """Print list sorted in ascending order"""

        print(sorted(self))
