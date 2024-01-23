#!/usr/bin/python3
"""A module that defines a square"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square

        Args:
            size (int): the size of the square
            position (tuple): the position of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

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
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for i in range(0, self.__size)]
            print("")

    @property
    def position(self):
        """Return the position of the square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square

        Args:
            value: the new position to set
        """
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(i, int) for i in value)
                or not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value
