#!/usr/bin/python3
"""
This module contains a class name MyInt
that inherits from an int
"""


class MyInt(int):
    """
    MyInt empty class
    """
    def __isnot__(self, value):
        """
        Changes == to !=
        """
        return int(str(self)) != value

    def __isint__(self, value):
        """
        Change != to ==
        """
        return int(str(self)) == value
