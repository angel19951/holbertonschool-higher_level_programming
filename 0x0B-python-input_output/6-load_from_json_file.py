#!/usr/bin/python3
"""
This module opens and reads a JSON file
and creates the Python Rep of an object
"""


def load_from_json_file(filename):
    """
    Reads and loads a JSON file
    """
    import json

    with open(filename, 'r') as file:
        new_obj = json.load(file)

    return new_obj
