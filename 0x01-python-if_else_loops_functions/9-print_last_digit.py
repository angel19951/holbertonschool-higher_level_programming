#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        temp = number * -1
        last = temp % 10
        print(last, end='')
        return last
    else:
        last = number % 10
        print(last, end='')
        return last
