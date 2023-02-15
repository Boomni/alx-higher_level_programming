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

    def update(self, *args, **kwargs):
        """
        Public method that assigns attributes:

        Args:
            *args is the list of arguments - no-keyworded arguments
                1st argument should be the id attribute
                2nd argument should be the size attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute
            **kwargs:
                variable number of key/value pairs
        Returns:
            The return statement is handled by __str__ method
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""

        my_dict = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return my_dict
