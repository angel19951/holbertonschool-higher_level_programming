#!/usr/bin/python3
"""This module contains a square class with the attribute size"""


class Square:
    """This is a square"""
    def __init__(self, size=0):
        """
        Takes in an int for instance attribute size
        Args:
        size (int): size of the square
        """
        self.__size = size
