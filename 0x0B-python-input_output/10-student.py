#!/usr/bin/python3
"""A module with a class that models a typical student"""


class Student:
    """A Class to model a student"""

    def __init__(self, first_name, last_name, age):
        """Initialise the class

        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary representation

        Description:
            This function retrieves a dictionary representation of Student
            instance.

        Args:
            attrs (list): an optional variable that is a list of strings

        Returns:
            only attribute names contained in this list if attrs is a
            list of strings, otherwise it returns all attributes

        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {m: getattr(self, m) for m in attrs if hasattr(self, m)}
        else:
            return self.__dict__
