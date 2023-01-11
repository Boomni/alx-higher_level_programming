#!/usr/bin/python3
"""My list"""


class MyList(list):
    """Inheritor class"""

    def print_sorted(self):
        """sorts and prints the list"""

        print(sorted(self))
