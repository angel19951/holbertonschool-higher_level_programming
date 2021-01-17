#!/usr/bin/python3
print_square = __import__('4-print_square').print_square


try:
    print_square(3)
    print()
    print_square(5)
    print()
    print_square(0)
    print_square(-3)
    print()
    print_square("Square")
    print_square('Sqaure')
    print_square("S")
    print_square('S')
    print_square([5, 6])
    print_square((5, 6))
    print_square()
except Exception as e:
    print(e)
print("")
