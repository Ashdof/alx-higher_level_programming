#!/usr/bin/python3
"""A module with a base class"""

import json


class Base:
    """The base class"""

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

    def to_json_string(list_dictionaries):
        """
        JSON string

        Description:
            This method creates a JSON string representation
            of a list of dictionaries

        Args:
            list_dictionaries (lis of dictionaries): a list of
            dictionary data

        Returns:
            JSON string representation of the data
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries, indent=4)
