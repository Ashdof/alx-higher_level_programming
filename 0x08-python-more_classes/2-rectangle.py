#!/usr/bin/python3
"""A module with a class"""


class Rectangle:
    """An class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle object

        Args:
            width (int): the width value
            height (int): the height value
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Return the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Update the width of the rectangle

        Args:
            value (int): the value to update the width
        """

        err_type = "width must be an integer"
        err_value = "width must be >= 0"

        if not isinstance(value, int):
            raise TypeError(err_type)
        elif value < 0:
            raise ValueError(err_value)
        else:
            self.__width = value

    @property
    def height(self):
        """Return the height of this rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Update the height of the rectangel

        Args:
            value (int): the value to update the rectangle
        """

        err_type = "height must be an integer"
        err_value = "height must be >= 0"

        if not isinstance(value, int):
            raise TypeError(err_type)
        elif value < 0:
            raise ValueError(err_value)
        else:
            self.__height = value

    def area(self):
        """Return the area of the rectangle"""

        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of the rectangle"""

        perimeter = (2 * self.__height) + (2 * self.__width)
        return perimeter
