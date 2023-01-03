#!/usr/bin/python3
"""A module with a class that defines a rectangle"""


class Rectangle:
    """A class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialise Class

        Description:
            This function initialises the class with default width and height
            values when it is invoked

        Args:
            width (int): a positive integer value
            height (int): a positive integer value

        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the width of this rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set Width Value

        Description:
            This method sets the width value of the rectangle

        Args:
            value (int): a positive integer value

        Raises:
            TypeError if value is not an integer
            ValueError if value is less than zero(0)

        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Return the height of this rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set Height Value

        Description:
            This method sets the height of the rectangle

        Args:
            value (int): a positive integer value

        Raises:
            TypeError if value is not of type integer
            ValueError if value is less than zero

        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
