"""
error_funcs.py

Contains functions that are used for the demonstration of errors.

AlgorithmHub. All rights reserved.
https://www.algorithmhub.com/
"""

from __future__ import division


def overflow_math_error():
    """
    Function that returns a values to demonstrate overflow error.
    This uses the math library.
    """

    import math
    return 1 - math.exp(-4 * 1000000 * -0.0641515994108)


def overflow_other_error():
    """
    Function that returns a values to demonstrate overflow error.
    This uses a simple power opertion of a float value.
    """
    return pow(16., 350)


def overflow_no_error():
    """
    Function that returns a values to demonstrate overflow error.
    This retuns a normal value, that does not cause an error.
    """

    return 100


def zero_division_error(num=1, den=1):
    """
    Function that returns a values to demonstrate zerodivision error.
    This retuns an error if no parameters are passed or if den=0,
    else returns the divided value.
    """

    return num / den


def floating_point_error(val=4.):
    """
    Function that raises an error when a floating point operation fails.
    """
    import numpy as np
    new_settings = np.seterr(all='raise')
    return np.sqrt(np.array([val]))
