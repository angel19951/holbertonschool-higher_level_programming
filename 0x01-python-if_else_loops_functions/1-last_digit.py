#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    l = number % -10
else:
    l = number % 10

print("Last digit of {} is ".format(number), end="")
if l > 5:
    print("{} and is greater than 5".format(l))
elif l == 0:
    print("{} and is 0".format(l))
elif l < 6 and l != 0:
    print(("{} and is less than 6 and not 0".format(l)))
