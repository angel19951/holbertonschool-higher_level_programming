#!/usr/bin/python3
"""
This module converts a JSON string
to the Python Rep of an object
"""


def from_json_string(my_str):
    """
    Converts JSON string to
    the Python Rep of an object
    """
    import json

    new_obj = json.loads(my_str)
    return new_obj
