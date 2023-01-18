#!/usr/bin/python3
"""Full rectangle"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class defines a rectangle and inherits from BaseGeometry.
    It has a constructor that initializes the width and height attributes
    Then validate that the values passed are integers with integer_validator
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("wigth", width)
        super().integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
