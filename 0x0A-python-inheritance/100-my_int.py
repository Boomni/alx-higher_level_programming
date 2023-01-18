#!/usr/bin/python3
"""My Integer"""


class MyInt(int):
    """Class that inverts "==" and "!="."""

    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return not super().__ne__(other)
