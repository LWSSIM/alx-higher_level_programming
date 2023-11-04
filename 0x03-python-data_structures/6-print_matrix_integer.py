#!/usr/bin/python3
# prints a matrix of ints
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for item in matrix:
            for i in item:
                print('{:d}'.format(i), end=" ")
            print("")
