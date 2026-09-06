"""
This module provides a solution to count dominant indices in an integer array.
An index is dominant if its value is greater than the average of all elements to its right.
"""


class Solution:
    """
    Provides functionality to analyze an array and find elements that
    are dominant over the average of the subsequent elements.
    """

    def is_dominant(self, value, right_sum, right_count):
        """
        Helper method to determine if a value is dominant.
        """
        if right_count == 0:
            return False
        return value > (right_sum / float(right_count))

    def dominantIndices(self, nums):
        """
        Counts the number of dominant indices in the given list.

        :type nums: List[int]
        :rtype: int
        """
        dominant_count = 0
        right_sum = 0
        right_count = 0

        # Iterate from right to left to calculate the running sum efficiently.
        for i in range(len(nums) - 1, -1, -1):
            current_val = nums[i]

            if self.is_dominant(current_val, right_sum, right_count):
                dominant_count += 1

            right_sum += current_val
            right_count += 1

        return dominant_count
