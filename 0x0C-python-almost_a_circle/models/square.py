#!/usr/bin/python3
""" A Square Module"""

from models.base import Base
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

    def __str__(self):
        """Return a string representation of this square instance"""

        info = "[Square] ({}) {}/{} - {}"
        return info.format(self.id, self.x, self.y, self.width)
