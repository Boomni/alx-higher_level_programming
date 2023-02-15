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
        """
        Returns an instance with all attributes already set
        """
        dummy_obj = cls(1, 1)
        dummy_obj.update(**dictionary)
        return dummy_obj

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        file = cls.__name__ + ".json"

        if file != None:
            with open(file, 'r') as f:
                content = cls.from_json_string(f.read())
            new_list = []#list to append the objs
            for item in content:
                dict1 = cls.create(**item)#create the obj 
                new_list.append(dict1)
            return new_list
        return []
