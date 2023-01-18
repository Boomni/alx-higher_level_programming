#!/usr/bin/python3
"""Square #1"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    This class defines a Square that inherits from Rectangle (9-rectangle.py):
        Instantiation with size: def __init__(self, size)::
            size must be private. No getter or setter
            size must be a positive integer, validated by integer_validator
        the area() method must be implemented
    """

    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        return (self.__size ** 2)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
