#!/usr/bin/python3
'''Test for ([..])
'''

import sys
sys.path.insert(0, '..')

Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

