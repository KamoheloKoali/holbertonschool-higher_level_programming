"""
module for reading json and csv files
"""

import json
import csv


def read_json(filepath, id=None):
    """
    read from json file

    args:
        filepath (str) - path to json file
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not id:
            return data
        
        for product in data:
            if product["id"] == id:
                return product
        
        return "Product not found"
            
    except (FileNotFoundError, KeyError):
        return None


def read_csv(filepath, id=None):
    """
    read from csv file

    args:
        filepath (str) - path to csv file
    """
    try:
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)
            data = list(reader) # convert to json

        if not id:
            return data
        
        for product in data:
            if product["id"] == id:
                return product

        return "Product not found"
    
    except (FileNotFoundError, KeyError):
        return None