#!/usr/bin/python3
for number in range(100):
    if number < 99:
        print("{:d}, ".format(number), end='')
    else:
        print(number)
