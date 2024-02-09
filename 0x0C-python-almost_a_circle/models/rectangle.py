#!/usr/bin/python3
"""A module with a rectangle class"""

from models.base import Base


class Rectangle(Base):
    """A class to model a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a rectangle object

        Args:
            width (int): the width of a rectangle object
            height (int): the height of a rectangle object
            x (int): the x coordinate of the rectangel object
            y (int): the y coordinate of the rectangel object
            id (int): the id of the rectangle object
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Return the width of this rectangle object"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set width

        Description:
            This function updates the width of this
            rectangle object

        Args:
            value (int): the value to update the width
        """

        if not isinstance(value, int):
            raise TypeError(f"{value} must be an integer")

        if value <= 0:
            raise ValueError(f"{value} must be > 0")

        self.__width = value

    @property
    def height(self):
        """Return the height of this rectangle object"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set height

        Description:
            This function updates the height of this
            rectangle object

        Args:
            value (int): the value to update the height
        """

        if not isinstance(value, int):
            raise TypeError(f"{value} must be an integer")

        if value <= 0:
            raise ValueError(f"{value} must be > 0")

        self.__height = value

    @property
    def x(self):
        """Return the x coordinate of this rectangle object"""

        return self.__x

    @x.setter
    def x(self, value):
        """Set x coordinate

        Description:
            This function updates the x coordinate of
            this rectangle object

        Args:
            value (int): the value to update the x coordinate
        """

        if not isinstance(value, int):
            raise TypeError(f"{value} must be an integer")

        if value <= 0:
            raise ValueError(f"{value} must be > 0")

        self.__x = value

    @property
    def y(self):
        """Return the y coordinate of this rectangle object"""

        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate

        Description:
            This function updates the y coordinates of
            this rectangle object

        Args:
            value (int): the value to update the y coordindate
        """

        if not isinstance(value, int):
            raise TypeError(f"{value} must be an integer")

        if value <= 0:
            raise ValueError(f"{value} must be > 0")

        self.__y = value
