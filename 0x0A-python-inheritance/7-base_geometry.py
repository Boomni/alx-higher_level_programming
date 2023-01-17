#!/usr/bin/python3
"""Improve Geometry module"""


class BaseGeometry:
    """defines BaseGeometry"""

    def area(self):
        """
        Raises Exception

        Args:
            self: Instance of an object
        Raises:
            Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value

        Args:
            self: instance of an object
            name: a string
            value: integer value to be validated
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 1
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
