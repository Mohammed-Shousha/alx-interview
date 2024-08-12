#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates an n by n 2D matrix in place.
    """
    if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) for row in matrix):
        return
    n = len(matrix)
    if not all(len(row) == n for row in matrix):
        return

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
