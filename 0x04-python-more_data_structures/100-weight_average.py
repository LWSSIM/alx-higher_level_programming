#!/usr/bin/python3
# ...returns the weighted average of all integers tuple (<score>, <weight>)
def weight_average(my_list=[]):
    if not my_list:
        return 0
    n = list(map(lambda x: (x[0] * x[1]), my_list))
    n = sum(n)
    x = 0
    for i in my_list:
        x += i[1]
    return n/x
