#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        # Set size as the value of the private instance attribute __size
        self.__size = size

    @property
    def size(self):
        # Return the value of the private instance attribute __size
        return self.__size

    @size.setter
    def size(self, value):
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
        size = self.__size
        # Calculate the area of the square by multiplying the size by itself
        return (size * size)
