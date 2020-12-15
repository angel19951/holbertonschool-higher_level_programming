#!/usr/bin/python3
def element_at(my_list, idx):
    count = 0
    if idx < 0:
        return None
    for r in my_list:
        count += 1
    if idx > count - 1:
        return None
    for i in my_list[-1]:
        if i == idx:
            element = my_list

    return element
