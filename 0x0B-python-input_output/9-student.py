#!/usr/bin/python3
"""A module with a class that defines a typical student"""

import json


class Student:
    """Model a Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize object

        Args:
            first_name (str): the first name of the student
            last_name (str): the last name of the student
            age (int): the age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of Student object"""

        return self.__dict__
