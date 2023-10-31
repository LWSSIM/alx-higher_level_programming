#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = abs(number) % 10
if number < 0:
    n = -n
STR = f"Last digit of {number} is {n} "
if n > 5:
    print(STR + "and is greater than 5")
elif n < 6 and n != 0:
    print(STR + "and is less than 6 and not 0")
else:
    print(STR + "and is 0")
