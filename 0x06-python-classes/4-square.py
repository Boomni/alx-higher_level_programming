#!/usr/bin/python3

"""Define a class Square"""


class Square:

    """Represent a square"""

    def __init__(self, size=0):
        """Initialize square set size as value of private instance attribute

        Args:
            size: private instance attribute, size of new square
        """

        self.__size = size

    @property
    def size(self):
        """Get and return the value of the private instance attribute __size"""

        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of square as value"""

        # Check if value is an integer
        if not isinstance(value, int):
            # If value is not an integer, raise a TypeError exception
            raise TypeError("size must be an integer")
        # Check if value is less than 0
        if value < 0:
            # If value is less than 0, raise a ValueError exception
            raise ValueError("size must be >= 0")
        # Set value as the value of the private instance attribute __size
        self.__size = value

    def area(self):
        """Returns the area of the square by multiplying the size by itself"""

        size = self.__size
        return (size * size)
