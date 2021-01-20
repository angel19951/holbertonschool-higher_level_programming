#!/usr/bin/python3
"""
This module opens and reads a .txt file
"""


def read_file(filename=""):
    """
    Opens and reads a file
    Args:
    filename (str): name of the file to open
    """
    with open(filename, 'r') as f:
        file = f.read()
