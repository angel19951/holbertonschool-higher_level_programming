#!/usr/bin/python3
"""
This module containse a class named MyList

Prints a sorted list.
"""


class MyList(list):
    """
    MyList class to be printed.
    """
    def print_sorted(self):
        """
        Print a list that is sorted
        """
        print(sorted(self))
