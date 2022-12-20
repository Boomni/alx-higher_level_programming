#!/usr/bin/python3

"""define a class Square"""


class Square:
    """represent a Square"""

    def __init__(self, size=0):
        """initialize new square

        Args:
            size: private instance attribute size
        """
        self.__size = size

    @property
    def size(self):
        """retrive size"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """set size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
