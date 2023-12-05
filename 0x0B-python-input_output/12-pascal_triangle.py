#!/usr/bin/python3
"""Module:Technical interview preparation:
    Pascal's triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal's triangle of n

    Args:
        n: assumed int

    Return: list of lists containing pascals triangle rep.
    """
    if n <= 0:
        return []

    P_Tri = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = P_Tri[i - 1][j - 1] + P_Tri[i - 1][j]
        P_Tri.append(row)

    return P_Tri
