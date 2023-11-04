#!/usr/bin/python3
# prints a matrix of ints
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    for item in matrix:
        for i in item:
            if i != item[-1]:
                print('{:d}'.format(i), end=" ")
            else:
                print('{:d}'.format(i))
