#!/usr/bin/python3
"""
This module returns a dictictionary with data struct
"""


def class_to_json(obj):
    """
    Returns dict with simple data struct
    """
    return obj.__dict__
