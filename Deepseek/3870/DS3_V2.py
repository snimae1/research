"""Module providing a solution for counting commas in formatted numbers."""


# pylint: disable=too-few-public-methods
class Solution:
    """Solution class for the LeetCode problem."""

    # pylint: disable=invalid-name
    def countCommas(self, n):
        """
        Return the total number of commas used when writing all integers from 1 to n.

        :type n: int
        :rtype: int
        """
        # Numbers below 1000 have no commas.
        if n < 1000:
            return 0

        # From 1000 up to n (inclusive) every number has exactly one comma,
        # because n <= 10^5 and all these numbers are below 1,000,000.
        return n - 999
