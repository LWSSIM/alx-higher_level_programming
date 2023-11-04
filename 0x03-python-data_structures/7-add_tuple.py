#!/usr/bin/python3
# adds two tupple elements
def add_tuple(tuple_a=(), tuple_b=()):
    a0, a1 = 0 if len(tuple_a) == 0 else tuple_a[0], 0 if len(
        tuple_a) <= 1 else tuple_a[1]
    b0, b1 = 0 if len(tuple_b) == 0 else tuple_b[0], 0 if len(
        tuple_b) <= 1 else tuple_b[1]
    result = (a0 + b0, a1 + b1)
    return (result)
