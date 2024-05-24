#!/usr/bin/python3
"""
6-max_integer.py finds the largest integer in a list

Examples:
    >>> max_integer([1, 2, 3, 4])
    4

    >>> max_integer([-1, -2, -3, -4])
    -1

    >>> max_integer([1.5, 2.5, 0.5])
    2.5

    >>> max_integer([])
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    ValueError: List cannot be empty

    >>> max_integer([1, 2, 'a'])
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    TypeError: All items in the list must be numbers
"""


def max_integer(list=[]):
    """
    Finds the largest integer in a list.

    Args:
        lst (list): List of numbers.

    Returns:
        The largest number in the list.

    Raises:
        ValueError: If the list is empty.
        TypeError: If an item in the list is not a number.
    """

    if not list or list is None:
        raise ValueError("List cannot be empty")

    for item in list:
        if not isinstance(item, (int, float)):
            raise TypeError("All items in the list must be numbers")

    max_num = list[0]

    for number in list:
        if number > max_num:
            max_num = number

    return max_num
