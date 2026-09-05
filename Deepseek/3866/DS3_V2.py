"""
Solution for finding the first unique even integer in an array.
"""
from collections import Counter

class Solution(object):
    """
    Provides methods for array processing tasks.
    """
    def firstUniqueEven(self, nums):
        """
        Return the first even integer that appears exactly once in nums.

        Args:
            nums (List[int]): List of integers.

        Returns:
            int: First unique even integer, or -1 if none exists.
        """
        # Count occurrences of each number
        freq = Counter(nums)

        # Iterate through the array in order to find the first unique even
        for num in nums:
            if num % 2 == 0 and freq[num] == 1:
                return num

        return -1
