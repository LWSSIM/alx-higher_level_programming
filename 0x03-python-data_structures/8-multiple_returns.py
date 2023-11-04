#!/usr/bin/python3
# returns tuple(str.len, str.1stchar)
def multiple_returns(sentence):
    char1st = sentence[0] if sentence[0] else None
    mul = (len(sentence), char1st)
    return (mul)
