#!/usr/bin/python3
def element_at(my_list, idx):
    count = 0
    if idx < 0:
        return None
    for r in my_list:
        count += 1
    if idx > count:
        return None
    for i in my_list:
        if i == idx:
            element = my_list[i]

    return element
