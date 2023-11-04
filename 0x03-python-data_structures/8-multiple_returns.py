#!/usr/bin/python3
# returns tuple(str.len, str.1stchar)
def multiple_returns(sentence):
    char1st = None if len(sentence) == 0 else sentence[0]
    mul = (len(sentence), char1st)
    return (mul)
