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
    return hasattr(obj, "__class__") and issubclass(obj.__class__, a_class)
