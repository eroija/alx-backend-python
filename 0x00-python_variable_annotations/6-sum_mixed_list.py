#!/usr/bin/env python3
"""Module for task 6."""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a mixed list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and
        floats to sum.

    Returns:
        float: The sum of the elements in the list.
    """
    return float(sum(mxd_lst))
