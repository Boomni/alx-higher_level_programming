#!/usr/bin/python3
"""Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new instance of the class.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square.
                Defaults to 0.
            y (int, optional): The y-coordinate of the square.
                Defaults to 0.
            id (int, optional): A specific id to assign to the instance.
                Inherited from the Rectangle class.
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: The size of the rectangle."""
        return self.__width

    @size.setter
    def size(self, value):
        """sets the size value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """Returns the string representation of square instance"""
        string = "[Square] ({}) {}/{} - {}"
        return string.format(self.id, self.x, self.y, self.size)
