#!/usr/bin/python3
"""Implement a Pascal's Triangle"""


def pascal_triangle(n):
    """Pascal's Triangle

    Description:
        This function returns a list of lists of integers representing
        the Pascal’s triangle of n

    Args:
        n (int): an integer value

    Returns:
        A list of list of integers
    """

    rs = []
    for i in range(n):
        row = [1]
        if rs:
            last_row = rs[-1]
            row.extend([sum(j) for j in zip(last_row, last_row[1:])])
            row.append(1)
        rs.append(row)
    return rs
