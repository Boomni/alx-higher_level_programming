#!/usr/bin/python3
"""Module for Serialization with JSON"""
import json


def to_json_string(my_obj):
    """This method takes a string object, returns the JSON representation"""
    
    return (json.dumps(my_obj))
