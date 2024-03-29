#!/usr/bin/python3
"""Square #1"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    This class defines a Square that inherits from Rectangle (9-rectangle.py):
        Instantiation with size: def __init__(self, size)::
            size is private. No getter or setter
            size is a positive integer, validated by integer_validator
        the area() is implemented
        print() prints, and str() returns, the square description
    """

    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        return (self.__size ** 2)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
