#!/usr/bin/python3
"""A module with a base class from which other classes will inherit"""

import json
import csv
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save to CSV file

        Description:
            This method serializes a CSV file

        Args:
            list_objs (list): a list of objects
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="", encoding="UTF-8") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Load from CSV file

        Description:
            This method deserialises an object from a CSV file

        Returns:
            A list of instantiated objects
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="", encoding="UTF-8") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    def draw(list_rectangles, list_squares):
        """Draw with turtle module

        Description:
            This method draws Rectangles and Squares using the
            turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """

        turt = turtle.Turtle()
        turt.screen.bgcolor("#154360")
        turt.pensize(5)
        turt.shape("turtle")

        turt.color("#FFC300")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(3):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#FF5733")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(3):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
