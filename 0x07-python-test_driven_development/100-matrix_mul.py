#!/usr/bin/python3
"""Matrix Multiplication"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices m_a and m_b.

    m_a and m_b must be lists of lists of integers or floats.
    m_a and m_b must be rectangles
    m_a and m_b must have the same number of rows.

    Return the result of the matrix multiplication of m_a and m_b.
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

    # Validate that m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')
    # Initialize result matrix with zeros
    result = [[0] * len(m_b[0]) for i in range(len(m_a))]

    # Perform matrix multiplication
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
