#!/usr/bin/python3
"""
This module containse the class named Base
and attribute id.

Validating the entry.
"""

import json


class Base:
    """
    This is a Base class
    Attribute:
    __nb_objects (int):
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """
        Returns the JSON string rep of a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
        else:
            new_str = json.dumps(list_dictionaries)
            return new_str
