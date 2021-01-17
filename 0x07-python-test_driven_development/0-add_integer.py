#!/usr/bin/python3
"""
This module add 2 integers
and validates entries or errors are raised.
"""


def add_integer(a, b=98):
    """
    Add 2 integers and validates if ints or floats
    Args:
    a (int, float): first number to add
    b (int, float): second int to add, preset value to int 98
    Returns: results of addition
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a + b)
