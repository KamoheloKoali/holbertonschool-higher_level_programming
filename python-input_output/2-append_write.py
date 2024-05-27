#!/usr/bin/python3
"""
2-append_write.py appends a string at the end of a text file (UTF8)
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)

    Args:
        filename (str): name of the file to write to
        text (str): text to append
    """

    written = 0
    with open(filename, "a", encoding="utf-8") as file:
        written = file.write(text)
    return written
