#!/usr/bin/python3

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
    spliter = [".", "?", ":"]
    substrings = []
    i = 0
    while i < len(text):
        c = text[i]
        if c in spliter:
            substrings.append(c)
            substrings.append("\n\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            substrings.append(c)
            i += 1
    print("".join(substrings))
