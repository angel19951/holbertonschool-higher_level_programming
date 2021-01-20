#!/usr/bin/python3
"""
This module verifies if a object is an intance of a class
that inherited from a specific class
"""


def inherits_from(obj, a_class):
    """
    Returns True is obj is instance of a specific class
    Args:
    obj: object to be analyzed
    a_class: class to check is obj is instance of
    """
    flag = False
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        flag = True
    return flag
