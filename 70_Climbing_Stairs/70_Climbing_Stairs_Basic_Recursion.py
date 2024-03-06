#!/usr/bin/python3

from typing import List

def climbStairs(n: int) -> int:
    """
    This function attempts to find ways of climbing
    stairs.

    Args:
        n: The number of stairs to climb

    Return:
        An integer value representing the various number
        of ways of climbing stairs
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return climbStairs(n-2) + climbStairs(n-1)

print("Example 1:")
n = 4
print("n = {}".format(n))
result = climbStairs(n)
print("The ways to climb {} stairs is {}.".format(n, result))
