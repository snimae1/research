"""
This module provides a solution to calculate the sum of all possible k-digit numbers
where each digit is chosen from a specified range [l, r].
"""

class Solution:
    """
    A class to solve the sum of numbers problem using modular arithmetic
    and geometric series.
    """

    def sum_of_numbers(self, left, right, k):
        """
        Calculate the sum of all k-digit numbers formed by digits in [left, right].

        :param left: The lower bound of the allowed digits (inclusive).
        :param right: The upper bound of the allowed digits (inclusive).
        :param k: The number of digits in each number.
        :return: The total sum modulo 10^9 + 7.
        """
        modulo = 10**9 + 7

        # Number of available digits for each position
        num_digits = right - left + 1

        # Sum of all available digits in the range [left, right]
        # Using the formula for the sum of an arithmetic progression
        digit_sum = (num_digits * (left + right)) // 2

        # Total sum formula: digit_sum * (num_digits^(k-1)) * (Sum of 10^i from i=0 to k-1)
        # The sum of the geometric series (10^0 + ... + 10^{k-1}) is (10^k - 1) / 9

        # 1. Contribution of the digit sum
        digit_sum_mod = digit_sum % modulo

        # 2. Contribution of the other (k-1) positions
        # We use pow(base, exp, mod) for efficient O(log k) computation
        ways_to_fill_others = pow(num_digits, k - 1, modulo)

        # 3. Contribution of the positional weights (geometric series)
        ten_pow_k = pow(10, k, modulo)
        numerator = (ten_pow_k - 1 + modulo) % modulo
        inv_9 = self._get_modular_inverse(9, modulo)
        geometric_series_sum = (numerator * inv_9) % modulo

        # Final total sum calculation
        total_sum = (digit_sum_mod * ways_to_fill_others) % modulo
        total_sum = (total_sum * geometric_series_sum) % modulo

        return total_sum

    def _get_modular_inverse(self, n, mod):
        """
        Calculate the modular multiplicative inverse using Fermat's Little Theorem.
        Valid only when mod is a prime number.
        """
        return pow(n, mod - 2, mod)
