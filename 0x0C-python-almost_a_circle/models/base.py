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
        if list_dictionaries is None:
            return None
        return json.dumps(list_dictionaries)

    def from_json_string(json_string):
        """Return the deserialization of a JSON string.
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None:
            return None
        return json.loads(json_string)
