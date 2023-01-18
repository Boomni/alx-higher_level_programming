#!/usr/bin/python3
"""Module that reads a textfile and print contents to stdout"""


def read_file(filename=""):
    with open(filename , "r", encoding="utf-8") as f:
        print(f.read())
