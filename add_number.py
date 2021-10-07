"""
A utility for summing up two numbers.
"""


def add_two_numbers(first, second):
    """Adds up both numbers and return the sum.
    Input values must be numbers."""
    if not isinstance(first, (int, float)) or not (isinstance(second, (int, float))):
        raise ValueError("Inputs must be numbers.")
    return first + second

