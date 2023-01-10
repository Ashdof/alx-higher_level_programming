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

    def to_json(self):
        """Retrieve a dictionary representation of a Student class"""
        return self.__dict__
