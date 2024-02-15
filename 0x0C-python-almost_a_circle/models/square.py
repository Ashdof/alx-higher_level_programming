#!/usr/bin/python3
""" A Square Module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that models a square object"""

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize square instance

        Args:
            size (int): the size of the square
            x (int): the x coordinate
            y (int): the y coordinate
            id (int): the id of the square instance
        """

        super().__init__(width=size, height=size, x=x, y=x, id=id)

    @property
    def size(self):
        """Return the size of this square instance"""

        return self.width

    @size.setter
    def size(self, value):
        """
        Update size of square

        Args:
            value (int): the value to set the size

        Raises:
            TypeError for an invalid data type
            ValueError for an invalid value: 0 or less
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update attributes

        Description:
            This function updates the attributes ofa square instance

        Args:
            args (int): a variable length of integer arguments
            kwargs (collection): a collection of key/value objects
            1st argument represents the id attribute
            2nd argument represents the size attribute
            3rd argument represents the x attribute
            4th argument represents the y attribute
        """

        if args and len(args) != 0:
            i = 0
            for arg in args:
                match i:
                    case 0:
                        self.id = arg
                    case 1:
                        self.width = arg
                        self.height = arg
                    case 2:
                        self.x = arg
                    case 3:
                        self.y = arg
                i += 1
        else:
            for key, vals in kwargs.items():
                match key:
                    case "id":
                        self.id = vals
                    case "size":
                        self.width = vals
                        self.height = vals
                    case "x":
                        self.x = vals
                    case "y":
                        self.y = vals

    def to_dictionary(self):
        """Return a dictionary representation of a square instance"""

        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """Return a string representation of this square instance"""

        info = "[Square] ({}) {}/{} - {}"
        return info.format(self.id, self.x, self.y, self.size)
