#!/usr/bin/python3
"""Module for deserialization with JSON"""
import json


def from_json_string(my_str):
    """This method takes a string object, returns the object representation"""

    return (json.loads(my_str))
