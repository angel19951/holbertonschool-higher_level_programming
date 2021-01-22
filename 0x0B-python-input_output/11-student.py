#!/usr/bin/python3
"""
This module contains a class named Student
and intances first_name, last_name, age
"""


class Student:
    """
    Class named Student
    Instances:
    first_name (str): name of the student
    last_name (str): last name of the student
    age (int): age of the student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object
        first_name (str): name of the student
        last_name (str): last name of the student
        age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dict with simple data struct
        """
        if type(attrs) is not list:
            return self.__dict__

        new_obj = {}

        for args in attrs:
            holder = getattr(self, args, None)
            if holder is not None:
                new_obj[args] = holder

        return new_obj

    def reload_from_json(selfm, json):
        """
        Reloads a JSON file
        """
        for arg in json:
            self.__dict__[arg] = json[arg]
