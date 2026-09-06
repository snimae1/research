"""
This module provides a solution to calculate the maximum total value
obtainable by selecting indices with decreasing values.
"""

class Solution:
    """
    Contains the logic to solve the maximum total value problem
    using binary search on the threshold value.
    """

    def maxTotalValue(self, value, decay, m):
        """
        This method is kept with the original name for compatibility,
        but calls the snake_case implementation.
        """
        return self.max_total_value(value, decay, m)

    def max_total_value(self, value, decay, m):
        """
        Calculates the max total value for given values and decay rates.

        :param value: List of initial values.
        :param decay: List of decay rates per selection.
        :param m: Maximum number of total selections allowed.
        :return: Maximum total value modulo 10^9 + 7.
        """
        mod = 10**9 + 7

        def get_count(threshold):
            """Calculates how many selections yield at least 'threshold' value."""
            count = 0
            for v, d in zip(value, decay):
                if v >= threshold:
                    count += (v - threshold) // d + 1
            return count

        # Binary search to find the optimal threshold X
        # We want the largest X such that count(X) >= m
        low, high = 1, max(value) if value else 0
        threshold = 0

        while low <= high:
            mid = (low + high) // 2
            if get_count(mid) >= m:
                threshold = mid
                low = mid + 1
            else:
                high = mid - 1

        if threshold == 0:
            return self._sum_all_positive(value, decay, mod)

        # Sum all values strictly greater than the threshold
        total_val = 0
        count_taken = 0
        threshold_plus_one = threshold + 1

        for v, d in zip(value, decay):
            if v >= threshold_plus_one:
                # k is the number of times we can pick this index to stay >= threshold+1
                k = (v - threshold_plus_one) // d + 1
                total_val += self._calculate_arithmetic_sum(v, d, k)
                count_taken += k

        # Fill the remaining slots up to m with the threshold value
        remaining = m - count_taken
        total_val += remaining * threshold

        return total_val % mod

    def _calculate_arithmetic_sum(self, first_term, diff, n):
        """ Calculates the sum of the first n terms of the arithmetic series. """
        # Sum formula: n/2 * (2*a + (n-1)*(-d))
        return (n * (2 * first_term - (n - 1) * diff)) // 2

    def _sum_all_positive(self, value, decay, mod):
        """ Sums all possible positive contributions if m is very large. """
        total = 0
        for v, d in zip(value, decay):
            if v > 0:
                k = (v - 1) // d + 1
                total += self._calculate_arithmetic_sum(v, d, k)
        return total % mod
