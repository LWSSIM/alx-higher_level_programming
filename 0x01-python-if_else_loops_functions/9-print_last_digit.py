#!/usr/bin/python3
def print_last_digit(number):
    i = abs(number) % 10
    print(i, end='')
    return i
