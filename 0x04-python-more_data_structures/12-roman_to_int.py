#!/usr/bin/python3
# ...converts a Roman numeral to an integer.
def roman_to_int(roman_string):

    if not roman_string or type(roman_string) is not str:
        return 0

    Ro_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    integer = 0
    prev = 0
    for char in reversed(roman_string):
        char = Ro_dict[char]
        if char >= prev:
            integer += char
        else:
            integer -= char
        prev = char
    return integer
