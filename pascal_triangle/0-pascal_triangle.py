#!/usr/bin/python3

from math import comb


def pascal_triangle(n):

    # case n < 1
    if n < 1:
        return []

    # recursive case
    triangle = pascal_triangle(n - 1)
    new_row = [comb(len(triangle) + 1, rowIndex) for rowIndex in range(1, n + 1)]
    triangle.append(new_row)
    return triangle
