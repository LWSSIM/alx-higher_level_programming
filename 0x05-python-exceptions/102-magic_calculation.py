#!/usr/bin/python3
# ...function converted from Python ByteCode
def magic_calculation(a, b):
    result = 0
    for i in range(1, 4):
        try:
            if i > a:
                raise Exception("Too far")
            result += (a + b) ** i / i
        except Exception:
            result += b + a
    return result
