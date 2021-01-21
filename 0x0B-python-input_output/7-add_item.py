#!/usr/bin/python3
"""
This module will read entries
from stdin and add them to a list to then
be added to a JSON file
"""

import sys

if __name__ == '__main__':
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    entry = []

    try:
        entry = load_from_json_file("add_item.json")
    except:
        entry = []

    for arg in sys.argv[1:]:
        entry.append(arg)

    save_to_json_file(entry, "add_item.json")
