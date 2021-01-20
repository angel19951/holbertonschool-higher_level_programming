#!/usr/bin/pthon3
"""
This module writes to a .txt file
"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="UTF8") as f:
        f.write(text)

    return len(text)
