#!/usr/bin/python3
"""
3-to_json_string.py returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)

    Args:
        my_obj (object): object to be turn into json string

    Returns:
        JSON representation of my_obj
    """

    return json.dumps(my_obj)
