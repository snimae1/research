"""
Module for finding the first element with a unique frequency.
"""

from typing import List
from collections import Counter

class Solution:  # pylint: disable=too-few-public-methods
    """
    Provides a method to find the first element whose frequency is unique.
    """

    def firstUniqueFreq(self, nums: List[int]) -> int:  # pylint: disable=invalid-name
        """
        Returns the first element (left to right) whose frequency is unique.

        Args:
            nums: List of integers.

        Returns:
            The first element with unique frequency, or -1 if none exists.
        """
        # Count frequencies of each number
        freq = Counter(nums)

        # Count how many numbers have each frequency value
        freq_count = Counter(freq.values())

        # Scan from left to right and check uniqueness
        for num in nums:
            if freq_count[freq[num]] == 1:
                return num

        # No element with unique frequency
        return -1
