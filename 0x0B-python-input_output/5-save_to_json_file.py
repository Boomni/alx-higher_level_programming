#!/usr/bin/python3
"""Module for Serialization of object with JSON into text file"""
import json


def save_to_json_file(my_obj, filename):
    """
    This method writes an Object to a text file, using a JSON representation

    Args:
        my_obj: object to write into file
        filename: name of text file

    """

    with open(filename, "w", encoding="utf-8") as f:
        string = json.dumps(my_obj)
        f.write(string)
