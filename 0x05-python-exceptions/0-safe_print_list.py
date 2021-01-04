#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    if x <= 0:
        return
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end='')
        except:
            i = i - 1
            break
    print()
    return i + 1
