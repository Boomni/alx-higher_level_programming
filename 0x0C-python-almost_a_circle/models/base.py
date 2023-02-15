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
        if list_dictionaries is not None or len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
