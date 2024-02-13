#!/usr/bin/python3

"""Base Model Definition

This module defines a base model class representing the
foundation for other classes within Project 0x0C*.

Private Class Attributes:
    __nb_objects (int): Number of instantiated base objects.
"""

import json
import csv
import turtle


class BaseModel:
    """Base Model Class

    This class represents the foundation for
    all other classes within the project.

    Attributes:
        id (int): Identity of the base object.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new base object.

        Args:
            id (int): Identity of the base object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            BaseModel.__nb_objects += 1
            self.id = BaseModel.__nb_objects

    @staticmethod
    def to_json_string(list_of_dicts):
        """Convert a list of dictionaries to a JSON string.

        Args:
            list_of_dicts (list): A list of dictionaries.

        Returns:
            str: JSON representation of the list of dictionaries.
        """
        if list_of_dicts is None or list_of_dicts == []:
            return "[]"
        return json.dumps(list_of_dicts)

    @classmethod
    def save_to_file(cls, list_of_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_of_objs (list): A list of objects.

        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_of_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_of_objs]
                jsonfile.write(BaseModel.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_str):
        """Deserialize a JSON string to a list of dictionaries.

        Args:
            json_str (str): JSON string.

        Returns:
            list: List of dictionaries.
        """
        if json_str is None or json_str == "[]":
            return []
        return json.loads(json_str)

    @classmethod
    def create(cls, **dictionary):
        """Create an object from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes.

        Returns:
            object: Instantiated object.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_obj = cls(1, 1)
            else:
                new_obj = cls(1)
            new_obj.update(**dictionary)
            return new_obj

    @classmethod
    def load_from_file(cls):
        """Load objects from a JSON file.

        Returns:
            list: List of instantiated objects.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = BaseModel.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_of_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_of_objs (list): A list of objects.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_of_objs is None or list_of_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_of_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Load objects from a CSV file.

        Returns:
            list: List of instantiated objects.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_of_rectangles, list_of_squares):
        """Draw rectangles and squares using the turtle module.

        Args:
            list_of_rectangles (list): List of Rectangle objects.
            list_of_squares (list): List of Square objects.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_of_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for _ in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_of_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for _ in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
