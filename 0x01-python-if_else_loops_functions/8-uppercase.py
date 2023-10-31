#!/usr/bin/env python3
def uppercase(str):
    for i in str:
        print("{}".format(chr(ord(i) - 32) if
            (97 <= ord(i) <= 122) else i), end='')
    print('')
