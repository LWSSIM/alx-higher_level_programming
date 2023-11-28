#!/usr/bin/python3
def magic_string(n=[]):
    n += [1]
    return "BestSchool" + (', BestSchool' * (len(n) - 1))
