#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates an M by N 2D matrix 90 degrees clockwise in place.
    """
    if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) for row in matrix):
        return
    m = len(matrix)
    n = len(matrix[0])
    if not all(len(row) == n for row in matrix):
        return

    # Create a new matrix to store the rotated version
    rotated_matrix = [[0] * m for _ in range(n)]

    # Rotate the matrix
    for i in range(m):
        for j in range(n):
            rotated_matrix[j][m - 1 - i] = matrix[i][j]

    # Copy the rotated matrix back to the original matrix
    matrix.clear()
    matrix.extend(rotated_matrix)
