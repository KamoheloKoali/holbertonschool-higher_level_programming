#!/usr/bin/python3
"""
7-add_item.py adds all arguments to a Python list
"""
import json
import sys
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

with open(sys.argv[1], "r") as file:
    save(load(file), "add_item.json")
