#!/usr/bin/python3
"""Module that writes to a file"""


def write_file(filename="", text=""):
    """
    Method that writes a string to a text file (UTF8)

    Args:
        filename: name of file
        text: text to write into the file
    Return:
        Number of Characters written

    """

    with open(filename, "w", encoding="utf-8") as f:
        char_num = f.write(text)
        return char_num
