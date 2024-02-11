#!/usr/bin/python3
"""A module with a base class from which other classes will inherit"""

import json


class Base:
    """The base class from which other classes will inherit"""

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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save to File

        Description:
            This method writes a json string representation of an
            instance to file

        Args:
            list_objs (json): a json object
        """

        f = cls.__name__ + ".json"

        with open(f, "w", encoding="UTF-8") as save_file:
            if list_objs is None:
                save_file.write("[]")
            else:
                list_of_dicts = []
                for item in list_objs:
                    list_of_dicts.append(item.to_dictionary())
                
                save_file.write(Base.to_json_string(list_of_dicts))

    def from_json_string(json_string):
        """Load from JSON

        Description:
            This method creates a list representation of a
            JSON string

        Args:
            json_string (json): a JSON string

        Returns:
            A list representation
        """

        if json_string is None or json_string == []:
            return []
        else:
            json.loads(json_string)
