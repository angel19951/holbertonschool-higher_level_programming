#!/usr/bion/python3
"""
This module prints a name compused of "First" and "Last" name
both will be validated of error will be raised
"""


def say_my_name(first_name, last_name=""):
    """
    Prints str "My name is "first_name" "last_name""
    Args:
    first_name (str): name, string
    last_name (str): last name, string preset value = ""
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
