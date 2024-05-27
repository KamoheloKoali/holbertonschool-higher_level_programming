#!/usr/bin/python3
"""
0-read_file.py reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): name of file to read
    """

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
