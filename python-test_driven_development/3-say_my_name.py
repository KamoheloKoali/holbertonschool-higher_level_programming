#!/usr/bin/python3
"""
3-say_my_name.py prints My name is <first name> <last name>

Examples:
    >>> say_my_name("John", "Smith")
    My name is John Smith
    >>> say_my_name("Walter", "White")
    My name is Walter White
    >>> say_my_name("Hank")
    My name is Hank
"""

def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>

    Args:
        first_name (string): first parameter
        last_name (string): second parameter

    Raises:
        TypeError: if either parameters are not strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
