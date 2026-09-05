"""
Solution module for finding the minimal distinct frequency pair.
"""

from collections import Counter
from typing import List

class Solution:  # pylint: disable=too-few-public-methods
    """
    Provides a method to find the pair (x, y) of distinct values from an array
    such that x < y, their frequencies differ, and x is minimal; if multiple x
    exist, y is minimal among those. Returns [-1, -1] if no such pair exists.
    """

    def minDistinctFreqPair(self, nums: List[int]) -> List[int]:  # pylint: disable=invalid-name
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Count frequencies of each value
        freq = Counter(nums)
        # Unique values sorted in ascending order
        values = sorted(freq.keys())

        # Try each possible x in increasing order
        for i, x in enumerate(values):
            # Look for the smallest y > x with a different frequency
            for y in values[i + 1:]:
                if freq[y] != freq[x]:
                    return [x, y]

        # No valid pair found
        return [-1, -1]
