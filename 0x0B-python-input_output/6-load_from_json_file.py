#!/usr/bin/python3
"""Module to create object from JSON file"""
import json


def load_from_json_file(filename):
    """Method that takes a JSON file, reads and creates an object"""

    with open(filename, "r", encoding="utf-8") as f:
        decoded = json.load(f)
        return (decoded)
