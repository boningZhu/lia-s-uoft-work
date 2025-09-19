#!/usr/bin/env python3
"""
Created by: Liary Ren
Created on: Sept 19, 2025
This program defines two functions:
1. is_odd(value): returns True if the value is odd, False otherwise.
2. convert_time(hour_24): converts a 24-hour clock hour to its 12-hour equivalent.

After completing the functions, test them in the Python shell using the examples
provided in their docstrings before submitting to MarkUs.
"""

def is_odd(value: int) -> bool:
    """Return True if and only if value is an odd number.
    
    >>> is_odd(108)
    False
    >>> is_odd(165)
    True
    """
    return value % 2 == 1


def convert_time(hour_24: int) -> int:
    """Return the 12-hour-clock hour that corresponds to the given 
    24-hour-clock hour hour_24.

    Precondition: 0 <= hour_24 <= 23

    >>> convert_time(0)
    12
    >>> convert_time(4)
    4
    >>> convert_time(12)
    12
    >>> convert_time(15)
    3
    """
    if hour_24 == 0:
        return 12
    elif hour_24 <= 12:
        return hour_24
    else:
        return hour_24 - 12


if __name__ == "__main__":
    # Quick tests so we can see results when running this file
    print("is_odd(108):", is_odd(108))    # Expected: False
    print("is_odd(165):", is_odd(165))    # Expected: True
    print("convert_time(0):", convert_time(0))    # Expected: 12
    print("convert_time(15):", convert_time(15))  # Expected: 3
