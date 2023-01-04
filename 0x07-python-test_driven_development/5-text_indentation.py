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

    skip_next_char = False

    for char in text:
        if skip_next_char:
            skip_next_char = False
            continue
        if char in {'.', '?', ':'}:
            print(char)
            print()
            # Set the skip_next_char flag to True to skip the next iteration
            skip_next_char = True
        # Otherwise, just print the character
        else:
            print(char, end="")
    print()
