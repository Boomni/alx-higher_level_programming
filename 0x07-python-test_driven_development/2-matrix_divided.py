#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """

    """ check if matrix is a list of lists of integers or floats """

    not_list = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(not_list)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(not_list)
    for row in matrix:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(not_list)
    if matrix == []:
        raise TypeError(not_list)

    """ check if all rows in matrix have the same size """
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    """ check if div is a number """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    """ check if div is not equal to 0 """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = []
    for row in matrix:
        new_row = []
        for item in row:
            divided_item = round(item / div, 2)
            new_row.append(divided_item)
        new.append(new_row)

    return (new)
