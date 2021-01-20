#!/usr/bin/python3
"""
This module verifies if a object is an instance,
or if the object is an instance of a class that inherited
from a specific class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True is obj is an instance or if is an instance
    of a class inherited from a specific class
    """
    return isinstance(obj, a_class)
