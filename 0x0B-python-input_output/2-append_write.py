#!/usr/bin/python3
"""Module that appends string to a text file"""


def append_write(filename="", text=""):
    """
    This method appends a string at the end of a textfile

    Args:
        filename: name of the file
        text: string to append
    Return:
        Number of characters added
    """

    with open(filename, "a", encoding="utf-8") as f:
        char_num = f.write(text)
        return (char_num)
