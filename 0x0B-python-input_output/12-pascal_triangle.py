#!/usr/bin/python3
"""
This module returns a list of list
representing a Pascal's triangle
"""


def pascal_triangle(n):
    """
    Returns list of list rep of Pascal's triangle
    """
    if n <= 0:
        triangle = [[]]
        return triangle

    triangle = [[1]]

    for count in range(1, n):
        t = [1]
        for move in range(1, count):
            t.append(triangle[count - 1][move - 1] + triangle[count - 1][move])
        t.append(1)
        triangle.append(t)
    return triangle
