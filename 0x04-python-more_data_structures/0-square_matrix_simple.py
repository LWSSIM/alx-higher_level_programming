#!/usr/bin/python3
# compute the square value of all integers of a matrix.
def square_matrix_simple(matrix=[]):
    new_matrix = (map(lambda i: list(map(lambda x: x**2, i)), matrix))
    return list(new_matrix)
