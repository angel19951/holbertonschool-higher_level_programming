#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
if num < 0:
    positive = num * -1
    l = positive % 10
else:
    l = num % 10

if l > 5:
    print("Last digit of ", num, " is {:d} and is greater than 5".format(l))
elif l == 0:
    print("Last digit of ", num, " is {:d} and is 0".format(l))
elif l < 6 and l > 0:
    print("Last digit of ", num, " is {:d} and is less than 6 and not 0".format(l))
