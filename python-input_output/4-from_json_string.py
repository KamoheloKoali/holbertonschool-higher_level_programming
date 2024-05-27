#!/usr/bin/python3
"""
4-from_json_string.py returns an object
"""
import json


def from_json_string(my_str):
    """
    Returns an object
    
    Args:
        my_str (str): json string

    Returns:
        an object
    """
    with open("new_text.txt", "w", encoding="utf-8") as file:
        file.write(my_str)
        return json.load(file)
