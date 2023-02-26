#!/usr/bin/python3
"""Module for Base class"""
import json
import csv
import turtle

class Base:
    """A base class for other classes to inherit from.

    This class provides a unique id for each instance, which is assigned
    automatically if not provided upon instantiation.

    Attributes:
        id (int): A unique id for each instance of the class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new instance of the class.

        Args:
            id (int, optional): A specific id to assign to the instance.
                If not provided, a unique id will be assigned automatically.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Public method that returns JSON string representation of
        list_dictionaries

        Args:
            list_dictionaries: list of dictionaries
        Returns:
            "[]": if None or empty
            JSON string representation: if not None or not empty

        """
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Public method that writes the JSON string representation of
        list_objs to a file

        Args:
            cls:
            list_objs: list of instances who inherits of Base
        """
        if list_objs is None or list_objs == []:
            jstr = "[]"
        else:
            jstr = cls.to_json_string([o.to_dictionary() for o in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string


        Args:
            json_string: a string representing a list of dictionaries

        Returns:
            the list represented by json_string
        """
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        try:
            filename = cls.__name__ + '.json'
            with open(filename, mode='r') as f:
                d = cls.from_json_string(f.read())
            return [cls.create(**x) for x in d]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
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
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
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
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        s = turtle.getscreen()
        t = turtle.getturtle()
        s.bgcolor("purple")
        t.pensize(3)

        t.color("yellow")
        for rect in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(rect.x, rect.y)
            t.down()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.hideturtle()

        t.color("fuchsia")
        for sq in list_squares:
            t.showturtle()
            t.up()
            t.goto(sq.x, sq.y)
            t.down()
            for i in range(2):
                t.forward(sq.width)
                t.left(90)
                t.forward(sq.height)
                t.left(90)
            t.hideturtle()
