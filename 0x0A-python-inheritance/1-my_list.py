#!/usr/bin/python3
"""My list"""


class MyList(list):
    """Inheritor class"""

    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """sorts and prints the list"""

        print(sorted(self))
