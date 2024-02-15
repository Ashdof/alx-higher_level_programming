#!/usr/bin/python3
"""A module with a base class from which other classes will inherit"""


class Base:
<<<<<<< HEAD
<<<<<<< HEAD
    """The base class from which other classes will inherit"""
=======
    """A class that serves as the base to model shapes"""
>>>>>>> 10e63ca (Improved documentation of modules)
=======
    """The base class"""
>>>>>>> 4394e1f (Revert "Improved documentation of modules")

    __nb_objects = 0

    def __init__(self, id=None):
        """Intialize the base model

        Args:
            id (int): the id of a model
        """

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
