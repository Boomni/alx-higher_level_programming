#!/usr/bin/python3
"""Integer Addition"""


def add_integer(a, b=98):
    """
    This function adds two integers and returns the result.

    Args:
    - a: An integer or a float to be added.
    - b: An integer or a float to be added. Default value is 98.

    Returns:
    - The sum of a and b as an integer.

    Raises:
    - TypeError: If a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    result = int(a) + int(b)
    return (result)
