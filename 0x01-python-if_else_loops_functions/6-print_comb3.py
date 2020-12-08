#!/usr/bin/python3
for dec in range(0, 9):
    for uni in range(dec + 1, 10):
        if dec == uni:
            pass
        else:
            if dec == 8 and uni == 9:
                print("{}{}".format(dec, uni))
                break
            print("{}{}, ".format(dec, uni), end=" ")
