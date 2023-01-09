#!/usr/bin/python3
"""A Class to model a geometry"""


class BaseGeometry:
    """Model a geometry object"""

    def area(self):
        """Raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value parameter

        Description:
            This function validates the parameter value

        Raises:
            TypeError exception if parameter value is not an integer
            ValueError exception if parameter value is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
