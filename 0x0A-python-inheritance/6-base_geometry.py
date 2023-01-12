#!/usr/bin/python3
"""Improve Geometry module"""


class BaseGeometry:
    """defines BaseGeometry"""

    def area(self):
        """
        Public instance method
        Args:
            self: Instance of an object
        Raises:
            Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")
