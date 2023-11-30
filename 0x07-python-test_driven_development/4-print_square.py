#!/usr/bin/python3
'''
    fn print squqre using #
'''


def print_square(size):
    '''
        print a square made of '#'

        Args:
            size: exclusive int

        Raises:
            bad input type + !size >= 0
    '''

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if not size:
        print()
        return

    for i in range(size):
        print("#" * size)
