#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        triangle.append([1 if j in (0, i) else triangle[i-1]
                        [j-1] + triangle[i-1][j] for j in range(i+1)])
    return triangle if n > 0 else []


print(pascal_triangle(10))
