#!/usr/bin/python3
""" How many instances """


class Rectangle:
    """class Rectangle that defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/set the width of the rectangle."""

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        rows = []
        for i in range(self.height):
            rows.append("#" * self.width)
        return "\n".join(rows)

    def __repr__(self):
        """Return a string representation of the rectangle \
                that can be used to recreate a new instance
                """
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """Print a message when the rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
