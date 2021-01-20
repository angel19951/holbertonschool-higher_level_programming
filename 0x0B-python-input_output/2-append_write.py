#!/usr/bin/python3
"""
This module appends to a .txt file
"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='UTF8') as f:
        f.write(text)

    return len(text)
