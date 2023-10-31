#!/usr/bin/python3
def fizzbuzz():
    STR = ("Fizz", "Buzz")
    for i in range(1, 101):
        n = ""
        if i % 3 == 0:
            n += STR[0]
        if i % 5 == 0:
            n += STR[1]
        if n:
            print(n, end=' ')
        else:
            print(i, end=' ')
