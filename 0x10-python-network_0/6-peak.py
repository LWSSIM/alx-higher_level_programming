#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """Returns peak value from a list of integers"""
    n = len(list_of_integers)

    for idx, num in enumerate(list_of_integers):
        prev = list_of_integers[idx - 1] if idx else 0
        next = list_of_integers[idx + 1] if idx < n - 1 else 0
        if num >= prev and num >= next:
            return num


print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
