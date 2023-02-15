#!/usr/bin/python3
"""Module for Base class"""
import json


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
        filename = cls.__name__ + ".json"
        list_of_dictionaries = []
        for items in list_objs:
            list_of_dictionaries.append(items.to_dictionary())
        json_str = cls.to_json_string(list_of_dictionaries)
        with open(filename, 'w') as f:
            f.write(json_str)
