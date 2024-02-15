#!/usr/bin/python3
"""A module with a base class from which other classes will inherit"""

import json


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

    @staticmethod
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

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create Instance

        Description:
            This method creates an instance of a class with
            all attributes

        Args:
            **dictionary (dict): Key/value of attributes to initialize

        Returns:
            An instance from a dictionary of attributes
        """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)

            return new

    @classmethod
    def load_from_file(cls):
        """Load from File

        Description:
            This method loads instances from a file

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """

        filename = str(cls.__name__) + ".json"

        try:
            with open(filename, "r", encoding="UTF-8") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]

        except IOError:
            return []
