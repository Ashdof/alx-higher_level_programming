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

        return self.width * self.height

    def update(self, *args, **kwargs):
        """
        Update Instance Attributes

        Description:
            This function updates the attributes of a retangle
            instance

        Args:
            args (int): a variable length of integer arguments
            kwargs (collection): a collection of key/value data
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        """

        if args and args != 0:
            i = 0
            for arg in args:
                match i:
                    case 0:
                        if arg is None:
                            self.__init__(self.width, self.height,
                                          self.x, self.y)
                        else:
                            self.id = arg
                    case 1:
                        self.width = arg
                    case 2:
                        self.height = arg
                    case 3:
                        self.x = arg
                    case 4:
                        self.y = arg
                i += 1
        else:
            for key, vals in kwargs.items():
                match key:
                    case "id":
                        if vals is None:
                            self.__init__(self.width, self.height,
                                          self.x, self.y)
                        else:
                            self.id = vals
                    case "width":
                        self.width = vals
                    case "height":
                        self.height = vals
                    case "x":
                        self.x = vals
                    case "y":
                        self.y = vals

    def display(self):
        """
        Display Object

        Description:
            This function displays a rectangle object using
            the # character
        """

        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            for j in range(self.width):
                print('#', end='')
            print("")

    def __str__(self):
        """Return a string representation of this rectangle object"""

        info = "[Rectangle] ({}) {}/{} - {}/{}"
        return info.format(self.id, self.x, self.y, self.width, self.height)

    def to_dictionary(self):
        """Return the dictionary representation of this rectangle instance"""

        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
