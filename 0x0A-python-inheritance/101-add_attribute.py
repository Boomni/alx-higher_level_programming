#!/usr/bin/python3
"""Can i?"""


def add_attribute(obj, attr, val):
    """Adds an attribute to a function if possible"""

    
    if not hasattr(obj, '__setattr__'):
        raise TypeError("can't add new attribute")
    obj.__setattr__(attr, val)
