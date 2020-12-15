#!/usr/bin/python3


def no_c(my_string):
    bye_c = ["c", "C"]
    new_string = my_string[:]

    new_string = ''.join(i for i in new_string if i not in bye_c)
    return new_string
