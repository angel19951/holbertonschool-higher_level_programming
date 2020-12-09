#!/usr/bin/python3
for i in range(122, 96, -1):
    if abs(i) % 2 == 0:
        i = abs(i) - 32
    print("{}".format(chr(abs(i))), end='')
