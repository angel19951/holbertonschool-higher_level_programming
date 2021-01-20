#!/usr/bin/python3
"""
This module verifies if an object is exactly isntance of a class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly instance of a class.
    Args:
    obj: any type to check if is instance
    a_class: class to check if obj is instance
    """
    return (type(obj) is a_class)
