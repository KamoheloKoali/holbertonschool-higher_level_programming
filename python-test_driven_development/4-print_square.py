#!/usr/bin/python3

"""
4-print_square.py prints a square with the character #

Examples:
    >>> print_square(3)
    ###
    ###
    ###
    >>> print_square(1)
    #
    >>> print_square(0)

"""

def print_square(size):
    """
    Prints a square with the character #

    Args:
        size (int): length of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
