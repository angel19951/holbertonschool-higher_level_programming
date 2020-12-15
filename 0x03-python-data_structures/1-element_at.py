#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0:
        return None
    if idx >= length:
        return None
    for i in my_list:
        if i == idx:
            element = my_list[idx]
            return element
