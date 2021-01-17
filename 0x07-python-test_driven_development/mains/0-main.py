#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer
print(add_integer(1, 2, 3))
try:
    print(add_integer(-2, 10))
    print(add_integer(10, -2))
    print(add_integer(-5. -3))
    print(add_integer(4.2, 3.55555))
    print(add_integer(10, -2.5))
    print(add_integer(20, "SUM"))
    print(add_integer(None, None))
    print(add_integer())
except Exception as e:
    print(e)
