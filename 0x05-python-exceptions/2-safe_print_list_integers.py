#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    loop = 0
    while count < x:
            try:
                print("{:d}".format(my_list[count]), end='')
                loop += 1
                count += 1
            except IndexError:
                raise
            except:
                count += 1
    print()
    return loop
