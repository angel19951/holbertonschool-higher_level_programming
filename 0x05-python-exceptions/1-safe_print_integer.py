#!/usr/bin/python3


def safe_print_integer(value):
    num = value
    try:
        print("{:d}".format(num))
        return True
    except:
        return False
