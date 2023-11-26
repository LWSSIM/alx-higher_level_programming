#!/usr/bin/python3
"""
    Module:
        safely adds 2 ints (check linked test dir)
"""



def add_integer(a, b=98):
    '''
        Adds 2 ints

        Args:
            arg1: a: int | float
            arg2: b: int | float default:98
            [if an arg is float cast it to int]

        Note:
            this fn is tested by Doctest method
            -find the related test_doc in /test/'ModuleName.txt'

        Return:
            addition result
    '''
    for i, operand in zip([a, b], ['a', 'b']):
        if type(i) not in [int, float]:
            raise TypeError("{} must be an integer".format(operand))
    return int(a) + int(b)

