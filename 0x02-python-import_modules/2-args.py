#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length - 1 == 0:
        print("0 arguments.")
    if length - 1 == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    if length - 1 > 1:
        print("{:d} arguments:".format(length - 1))
        for i in range(1, length):
            print("{:d}: {}".format(i, sys.argv[i]))
