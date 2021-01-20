#!/usr/bin/python3
"""
This module appends to a .txt file
"""


def append_write(filename="", text=""):
    """
    Appends a string to an .txt file
    Args:
    filename (str): name of the file to append to
    text (str): text to append to file
    """
    with open(filename, 'a', encoding='UTF8') as f:
        return f.write(text)
