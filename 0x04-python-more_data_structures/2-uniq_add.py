#!/usr/bin/python3


def uniq_add(my_list=[]):
    new_list = []
    add = 0

    for element in my_list:
        if element not in new_list:
            new_list.append(element)

    for element in new_list:
        add += element
    return add