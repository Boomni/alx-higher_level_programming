#!/usr/bin/python3
"""Module that reads a textfile and print contents to stdout"""


def read_file(filename=""):
    """
    This method takes filename as argument
    Reads and prints its contents to stdout
    """

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
