"""
module for reading json and csv files
"""

import json
import csv


def read_json(filepath):
    """
    read from json file

    args:
        filepath (str) - path to json file
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return None


def read_csv(filepath):
    """
    read from csv file

    args:
        filepath (str) - path to csv file
    """
    try:
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)
            data = list(reader)
        return data
    
    except FileNotFoundError:
        return None