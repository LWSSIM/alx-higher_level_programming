#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str):
        return str
    copy = ""
    for char in range(len(str)):
        if char != n:
            copy += str[char]
    return copy
