#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: object to be checked
        a_class: class to check against
    Returns:
        True: if the object is an instance of, \
                a class that inherited from, the specified class
        Otherwise False
    """
    if isinstance(obj, a_class):
        return True
    return False
