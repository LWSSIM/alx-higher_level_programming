#!/usr/bin/python3
'''
    testing 2-matrix_divider
'''

import sys

sys.path.insert(0, '..')

matrix_divider = __import__("2-matrix_divided").matrix_divided

matrix_1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print(matrix_divider(matrix_1, 1))

matrix_1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print(matrix_divider(matrix_1, 2))

matrix_1 = [[1.897, 1.75, 1.3], [22.8, 2.23, 2.78963], [3.102, 30.5, 3.7183684]]
print(matrix_divider(matrix_1, 2.1))

matrix_1 = [[1, 11], [2, 2, 2], [3, 3, 3]]
print(matrix_divider(matrix_1, 6))

matrix_1 = []
print(matrix_divider(matrix_1, 2))

matrix_1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print(matrix_divider(matrix_1, 0))

matrix_1 = [[1, "prst", 1], [2, 2, 2], [3, 3, 3]]
print(matrix_divider(matrix_1, 1))

