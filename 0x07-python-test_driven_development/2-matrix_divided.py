#!/usr/bin/python3
'''
    Module:
        fn to divide input matrix elements
'''
def matrix_divided(matrix, div):
    '''
        function that divides all elements of a matrix.

        Args:
            matrix: input (list of lists) made of int || floats
            div: number(int || float) != 0

        Return:
            a new martix

        Raises:
            type err on bad input parameter type
            div/zero if div = 0
    '''
    err = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(err)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(err)
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError(err)

    mtrx_size = len(matrix)
    row_lenght_0 = len(matrix[0])
    x = 1
    while x < mtrx_size - 1:
        if len(matrix[x]) !=  row_lenght_0:
            raise TypeError(err2)
        x += 1

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda i: round(i / div, 2), row)) for row in  matrix])

