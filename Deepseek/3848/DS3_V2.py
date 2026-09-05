"""
Module for solving the digitorial permutation problem.
"""

import math

class Solution:  # pylint: disable=too-few-public-methods
    """
    Provides a method to check if any permutation of a given integer's digits
    forms a digitorial number (where the sum of factorials of its digits equals
    the number itself).
    """

    def isDigitorialPermutation(self, n):  # pylint: disable=invalid-name
        """
        Determine whether any permutation of the digits of n (including the
        original order) forms a digitorial number.

        A number is digitorial if the sum of the factorials of its digits is
        equal to the number itself. This method checks if there exists a
        permutation of n (without leading zero) that satisfies this condition.

        :param n: Integer to check (1 <= n <= 10^9)
        :return: True if such a permutation exists, False otherwise.
        """
        # Convert n to its digit list
        digits = list(str(n))

        # Compute the sum of factorials of each digit
        digit_factorial_sum = sum(math.factorial(int(d)) for d in digits)

        # Convert the sum to a digit list
        sum_digits = list(str(digit_factorial_sum))

        # A valid permutation exists iff the multisets of digits match.
        # If they match, we can always arrange the digits to avoid a leading
        # zero because n >= 1 ensures at least one non-zero digit in the sum.
        return sorted(digits) == sorted(sum_digits)
