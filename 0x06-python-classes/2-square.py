#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        # Check if size is an integer
        if not isinstance(size, int):
            # If size is not an integer, raise a TypeError exception
            raise TypeError("size must be an integer")
        # Check if size is less than 0
        if size < 0:
            # If size is less than 0, raise a ValueError exception
            raise ValueError("size must be >= 0")
        # Set size as the value of the private instance attribute __size
        self.__size = size
