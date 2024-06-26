#!/usr/bin/python3

"""
0-add_integer.py adds two integers and returns the result

Examples:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the result

    Args:
        a (int): first parameter
        b (int): second parameter. Defaults to 98

    Returns:
        The return value. integer value on success

    Raises:
        TypeError: if either a or b are not int or float
        ValueError: if either a or b is None
    """

    if not isinstance(a, (float, int)):
        if a is not None:
            raise TypeError("a must be an integer")
        raise ValueError("a must be an integer")

    if not isinstance(b, (float, int)):
        if b is not None:
            raise TypeError("b must be an integer")
        raise ValueError("b must be an integer")

    if type(a) is float and type(b) is float:
        return int(a) + int(b)

    elif type(a) is not float and type(b) is float:
        return a + int(b)

    elif type(a) is float and type(b) is not float:
        return int(a) + b

    return a + b
