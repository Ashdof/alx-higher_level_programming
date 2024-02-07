#!/usr/bin/python3
"""A module with a Student class"""

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

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of Student object"""

        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {m: getattr(self, m) for m in attrs if hasattr(self, m)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Reload from JSON

        Description:
            This function replaces all attributes of a student instance

        Args:
            json (dict): the key/value pairs to replace the attributes
        """

        for i in json:
            self.__dict__[i] = json[i]
