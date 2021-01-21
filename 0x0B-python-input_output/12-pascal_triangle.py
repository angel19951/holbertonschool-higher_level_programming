#!/usr/bin/python3
"""
This module returns a list of list
representing a Pascal's triangle
"""


def pascal_triangle(n):
    """
    Returns list of list rep of Pascal's triangle
    """
    triangle = [[1]]

    for count in range(1, n):
        tri = [1]
        for move in range(1, count):
            tri.append(triangle[count - 1][move - 1] + triangle[count - 1][move])
        tri.append(1)
        triangle.append(tri)
    return triangle
