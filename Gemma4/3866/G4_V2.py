"""
This module provides a solution to find the first unique even integer in a list.
"""

# pylint: disable=too-few-public-methods
class Solution:
    """
    A class used to represent a solution for finding the first unique even integer.
    """

    # pylint: disable=invalid-name
    def firstUniqueEven(self, nums):
        """
        Returns the first even integer that appears exactly once in the list.

        :type nums: List[int]
        :rtype: int
        """
        # Dictionary to store the frequency of each number
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # Iterate through the list again to maintain original order (index)
        for num in nums:
            # Check if the number is even AND appears exactly once
            if num % 2 == 0 and counts[num] == 1:
                return num

        # Return -1 if no such integer exists
        return -1
