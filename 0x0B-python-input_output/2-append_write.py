#!/usr/bin/python3
"""
This module appends to a .txt file
"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='UTF8') as f:
        f.write(text)
<<<<<<< HEAD

    return len(text)
=======
        return len(text)
>>>>>>> 5c1640c56508c1d2a5d3b82837ca0f00e1b0c850
