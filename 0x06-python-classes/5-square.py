#!/usr/bin/python3
"""A module that defines a square"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """Initialize the square

        Args:
            sie (int): the size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return the area of the square"""

        return self.__size**2

    @property
    def size(self):
        """Return the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square

        Args:
            value (int): the new value to set the size of the square
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Print the square with the # character"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
