#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys


def get_input():
    """Retrieves and validates this program's argument.

    Returns:
        int: The size of the chessboard.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos0, pos1):
    """Checks if the positions of two queens are in an attacking mode.

    Args:
        pos0 (list or tuple): The first queen's position.
        pos1 (list or tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position else False.
    """
    return (pos0[0] == pos1[0] or pos0[1] == pos1[1] or
            abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1]))


def group_exists(solutions, group, n):
    """Checks if a group exists in the list of solutions.

    Args:
        solutions (list of lists): The list of possible solutions.
        group (list of integers): A group of possible positions.
        n (int): The size of the chessboard.

    Returns:
        bool: True if it exists, otherwise False.
    """
    for stn in solutions:
        if all(any(stn_pos == grp_pos for stn_pos in stn) for grp_pos in group):
            return True
    return False


def build_solution(solutions, pos, n, row=0, group=None):
    """Builds a solution for the n queens problem.

    Args:
        solutions (list of lists): The list of possible solutions.
        pos (list of lists): The list of possible positions.
        n (int): The size of the chessboard.
        row (int): The current row in the chessboard.
        group (list of lists of integers): The group of valid positions.
    """
    if group is None:
        group = []

    if row == n:
        tmp0 = group.copy()
        if not group_exists(solutions, tmp0, n):
            solutions.append(tmp0)
    else:
        for col in range(n):
            a = row * n + col
            if all(not is_attacking(pos[a], grp_pos) for grp_pos in group):
                build_solution(solutions, pos, n, row + 1, group + [pos[a]])


def get_solutions(n):
    """Gets the solutions for the given chessboard size.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list of lists: The list of possible solutions.
    """
    pos = [[i // n, i % n] for i in range(n ** 2)]
    solutions = []
    build_solution(solutions, pos, n)
    return solutions


def main():
    n = get_input()
    solutions = get_solutions(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
