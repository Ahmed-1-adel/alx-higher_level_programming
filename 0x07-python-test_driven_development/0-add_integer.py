#!/usr/bin/python3
"""Module for add_integer method."""

def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: the first integer.
        b: the second integer, default 98.

    Raises:
        TypeError: if a, b are not int, float.

    Returns:
        The sum of the two integers.
    """

    if not isinstance(a, int) and not isinstance(b, int):
        raise TypeError("a must be an integer")
    if not isinstance(a, float) and not isinstance(b, float):
        raise TypeError("a must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
