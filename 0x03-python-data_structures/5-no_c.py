#!/usr/bin/python3
# removes c&C chars from str
def no_c(my_string):
    copy = ""
    for i in my_string:
        if i not in 'cC':
            copy += i
    return (copy)
