#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for elements in my_list:
        print("{:d}".format(my_list[elements - 1]))
