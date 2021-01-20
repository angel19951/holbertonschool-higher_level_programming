#!/usr/bin/python3
"""
This module writes to a .txt file
"""


def write_file(filename="", text=""):
    """
    Opens and writes to a file
    Args:
    filename (str): name of the file to write in
    text (str): string to write in the file
    """
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)
