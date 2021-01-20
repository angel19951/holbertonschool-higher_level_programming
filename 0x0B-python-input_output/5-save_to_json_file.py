#!/usr/bin/python3
"""
This module writes an Object
to a text file using JSON Rep
"""


def save_to_json_file(my_obj, filename):
    """
    Saves an object to a .txt file
    using JSON Rep
    """
    import json

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
