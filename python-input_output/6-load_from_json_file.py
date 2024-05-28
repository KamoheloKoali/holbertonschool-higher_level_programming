#!/bin/usr/python3
"""
6-load_from_json_file.py creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”

    Args:
        filename (str): name of json file

    Returns:
        a python object
    """

    with open(filename, "r") as file:
        return json.load(file)
