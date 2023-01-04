#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """
    Indent the given text by adding two newlines after ".", "?", and ":".

    Args:
    - text (str): The text to be indented.

    Returns:
    None

    Raises:
    - TypeError: If `text` is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
