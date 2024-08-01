#!/usr/bin/env python3
"""Module for task 5."""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floats.

    Args:
        input_list (List[float]): list of floats to sum.

    Returns:
        float: The sum of the elements in the list.
    """
    return float(sum(input_list))
