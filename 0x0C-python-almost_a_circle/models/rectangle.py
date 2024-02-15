#!/usr/bin/python3
"""A module with a class that models a rectangle"""

from models.base import Base


class Rectangle(Base):
    """A class to model a rectangle and inherits from a base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialise class

        Description:
            This method is the class constructor which initialises
            the class with the required parameters

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangel
            x (int): the x coordinate of the rectangle
            y (int): the y coordinate of the rectangle
            id (int): the instance tracker

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width of rectangle

        Description:
            This method obtains the width of the rectangle

        Returns:
            The width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """Set width

        Description:
            This method sets the width of the rectangle

        Args:
            value (int): a positive ineteger value to set the
            width of the rectangle

        Raises:
            TypeError if height_value is not an integer
            ValueError if height_value is 0 or negative

        """

        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Height of rectangle

        Description:
            This method obtains the height of the rectangle

        Returns:
            The height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """Set height

        Description:
            This method sets the height of the rectangle

        Args:
            value (int): a positive integer value to set the
            height of the rectangle

        Raises:
            TypeError if height_value is not an integer
            ValueError if height_value is 0 or negative
        """

        if type(value) != int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """X-coordinate

        Description:
            This method obtains the x coordinate of the rectangle

        Returns:
            The x coordinate
        """

        return self.__x

    @x.setter
    def x(self, value):
        """Set X-coordinate

        Description:
            This method sets the x coordinate of the rectangle with
            the value passed as parameter

        Args:
            value (int): a positive integer value to set the x
            coordinate of the rectangle

        Raises:
            TypeError if value is not an integer
            ValueError if value is 0 or negative
        """

        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Y-coordinate

        Description:
            This method obtains the y coordinate of the rectangle

        Returns:
            The y coordinate
        """

        return self.__y

    @y.setter
    def y(self, value):
        """Set Y-coordinate

        Description:
            This method sets the y coordinate of the rectangle with
            the value passed as parameter

        Args:
            value (int): a positive integer value to set the y
            coordinate of the rectangle

        Raises:
            TypeError if value is not an integer
            ValueError if value is 0 or negative
        """

        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Compute area

        Description:
            This function computes the area of a rectangle
            instance

        Returns:
            The computed area
        """

        return self.__width * self.__height
