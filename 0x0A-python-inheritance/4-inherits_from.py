#!/usr/bin/python3
"""Only subclass of"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited \
            (directly or indirectly) from the specified class.

    :param obj: The object to check.
    :type obj: object
    :param a_class: The class to check against.
    :type a_class: class
    :return: True if the object is an instance of a class that inherited \
            (directly or indirectly) from the specified class, otherwise False.
    :rtype: bool
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
