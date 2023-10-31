#!/usr/bin/python3
import random  # Module to generate random number
number = random.randint(-10, 10)
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")
