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
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif clipboard > 0:
            done += clipboard
            ops_count += 1
    return ops_count
