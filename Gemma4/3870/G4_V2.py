"""
This module provides a solution to calculate the total number of commas
used when writing all integers from 1 to n in standard formatting.
"""

# pylint: disable=too-few-public-methods
class Solution:
    """
    Provides a method to count the total number of commas in a range of integers.
    """

    # pylint: disable=invalid-name
    def countCommas(self, n):
        """
        Calculates the total number of commas used in standard formatting
        for all integers from 1 up to n.

        :type n: int
        :rtype: int
        """
        total_commas = 0
        # Standard formatting inserts a comma every 3 digits from the right.
        # 1,000 to 999,999 -> 1 comma
        # 1,000,000 to 999,999,999 -> 2 commas, etc.

        k = 1
        while True:
            lower_bound = 10**(3 * k)
            if lower_bound > n:
                break

            upper_bound = 10**(3 * (k + 1)) - 1
            # Calculate how many numbers in the range [lower_bound, upper_bound]
            # exist up to the limit 'n'.
            count_in_range = min(n, upper_bound) - lower_bound + 1

            # Each number in this specific range contributes at least k commas.
            total_commas += count_in_range * k
            k += 1

        return total_commas
