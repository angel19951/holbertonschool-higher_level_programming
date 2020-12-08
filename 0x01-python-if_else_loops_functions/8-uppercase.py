#!/usr/bin/python3
def uppercase(str):
    for c in str:
        var = ord(c)
        if c.islower():
            var = var -32
        print("{:c}".format(var), end="")
    print()
