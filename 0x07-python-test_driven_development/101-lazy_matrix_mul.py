#!/usr/bin/python3
"""Lazy matrix multiplication"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
    - m_a (list): A list of lists containing integers or floats.
    - m_b (list): A list of lists containing integers or floats.

    Returns:
    - list: A list of lists containing the result of the matrix multiplication.

    Raises:
    - TypeError: If `m_a` or `m_b` is not a list.
    - TypeError: If `m_a` or `m_b` is not a list of lists.
    - ValueError: If `m_a` or `m_b` is an empty list.
    - TypeError: If `m_a` or `m_b` contains an element not integer or float.
    - TypeError: If rows of `m_a` or `m_b` are not all the same size.
    - ValueError: If number of columns in `m_a` is != number of rows in `m_b`.
    """
    # Validate m_a
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError('m_a must be a list of lists')
    if not m_a or not all(row for row in m_a):
        raise ValueError('m_a can\'t be empty')
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError('m_a should contain only integers or floats')
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError('each row of m_a must be of the same size')

    # Validate m_b
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_b must be a list of lists')
    if not m_b or not all(row for row in m_b):
        raise ValueError('m_b can\'t be empty')
    if not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError('m_b should contain only integers or floats')
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError('each row of m_b must be of the same size')

    # Check that number of columns in m_a is == number of rows in m_b
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Use NumPy to perform the matrix multiplication and return the result
    return np.matmul(m_a, m_b).tolist()
