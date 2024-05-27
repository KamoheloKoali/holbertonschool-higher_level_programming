#!/usr/bin/python3
"""
1-write_file.py writes a string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)

    Args:
        filename (str): name of file to write to
        text (str): what to write to file
    """

    written = 0
    with open(filename, "w", encoding="utf-8") as file:
        written = file.write(text)
    return written
