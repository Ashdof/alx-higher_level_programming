#!/usr/bin/python3
"""A base class that defines a geometry"""


class BaseGeometry:
    """A base class that defines a geometry"""

    def area(self):
        """Raise an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate a value

        Args:
            name (str): the name of the value
            value (int): the value to validate
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
