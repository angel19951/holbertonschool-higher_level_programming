#!/usr/bin/python3


def roman_to_int(roman_string):
    roman_round = {"I":1, "V":5, "X":10, "L": 50, "C":100, "D":500, "M": 1000}
    roman_special = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
    i = 0
    num = 0

    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_string[i:i+2] in roman_special:
            num += roman_special[roman_string[i:i+2]]
            i += 2
        else:
            num += roman_round[roman_string[i]]
            i += 1
    return num
