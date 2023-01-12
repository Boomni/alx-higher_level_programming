#!/usr/bin/python3
"""Exact same object"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: object to be checked
        a_class: class to check against

    Returns:
         True if obj is exactly an instance of a_class; False otherwise
    """
    if isinstance(type(obj), a_class):
        return True
    else:
        return False
