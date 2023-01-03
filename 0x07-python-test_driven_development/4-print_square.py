#!/usr/bin/python3
"""
Write a function that prints a square with the character #.

Prototype: def print_square(size):
    size is the size length of the square
    size must be an integer, otherwise raise a TypeError exception
    if size is less than 0, raise a ValueError exception
    if size is a float and is less than 0, raise a TypeError exception
    You are not allowed to import any module
"""


def print_square(size):
    """
    Function that prints a square with the character #

    Arg:
        size: size length of the square
    Raises:
        TypeError: if size is not integer
        ValueError: if size < 0
        TypeError: if size is float and is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
