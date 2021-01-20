#!/usr/bin/python3
"""
This module converts a dict
to the JSON Rep of an object
"""


def to_json_string(my_obj):
    """
    Converts a dict to a JSON Rep of an object
    """
    import json


    new_obj = json.dumps(my_obj)
    return new_obj
