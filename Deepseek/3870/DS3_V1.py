class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Numbers with fewer than 4 digits (1..999) have no commas.
        if n < 1000:
            return 0
        # Every integer from 1000 up to n (inclusive) contains exactly one comma
        # because n <= 10^5, and numbers in [1000, 999999] have 1 comma.
        return n - 999
