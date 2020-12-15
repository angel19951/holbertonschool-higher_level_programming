#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    length = len(my_list)

    if idx < 0:
        return my_list
    if idx >= length:
        return my_list
    for i in my_list:
        if i == idx:
            my_list[idx] = element
            return my_list
