#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    length = len(argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    fir_num = int(argv[1])
    sec_num = int(argv[3])

    operation = argv[2]
    if operation == "+":
        result = add(fir_num, sec_num)
    elif operation == "-":
        result = sub(fir_num, sec_num)
    elif operation == "*":
        result = mul(fir_num, sec_num)
    elif operation == "/":
        result = div(fir_num, sec_num)
    else:
        print("Unknown operator. Only: +, -, * and / available")
        exit(1)
    print("{:d} {} {:d} = {}".format(fir_num, operation, sec_num, result))
