"""
module for reading json and csv files
"""

import json
import csv
import sqlite3


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
                return [product]
        
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
        print(data)
        for product in data:
            if product["id"] == str(id):
                return [product]
        

        return "Product not found"
    
    except (FileNotFoundError, KeyError):
        return None
    
def read_db(id=None):
    """
    read data from database
    """
    
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    data = []
    diction = {}
    
    if not id:
        res = cursor.execute("SELECT * FROM Products")
        
        for item in res:
            diction["id"] = item[0]
            diction["name"] = item[1]
            diction["category"] = item[2]
            diction["price"] = item[3]
            data.append(dict((diction)))
            
        return data
    
    res = cursor.execute("SELECT * FROM Products WHERE id == {:d}".format(id))
    
    if not res:
        return None
    
    for item in res:
        diction["id"] = item[0]
        diction["name"] = item[1]
        diction["category"] = item[2]
        diction["price"] = item[3]
        data.append(dict((diction)))
        
    return data
    # [(1, 'Laptop', 'Electronics', 799.99), (2, 'Coffee Mug', 'Home Goods', 15.99)]