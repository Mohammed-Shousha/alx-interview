#!/usr/bin/python3

'''The minimum operations coding challenge.'''


def minOperations(n):
    """
    Calculates the minimum number of operations to get n 'H' characters.

    Args:
        n: The target number of 'H' characters.

    Returns:
        The minimum number of operations needed, or 0 if impossible.
    """
    if n <= 0:
        return 0

    min_operations = [0] * (n + 1)

    for i in range(2, n + 1):
        min_operations[i] = float('inf')

        for j in range(1, i):
            if i % j == 0:
                min_operations[i] = min(
                    min_operations[i], min_operations[j] + i // j)

    return min_operations[n] if min_operations[n] != float('inf') else 0
