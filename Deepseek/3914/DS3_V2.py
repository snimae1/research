"""
Solution for LeetCode problem: Minimum Operations to Make Array Non-decreasing.
"""
# pylint: disable=invalid-name, too-few-public-methods

class Solution:
    """
    Provides method to compute minimum sum of x for operations to make array non-decreasing.
    """
    def minOperations(self, nums):
        """
        Given an array nums, return the minimum possible sum of x values across
        all operations needed to make the array non-decreasing.

        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                total += nums[i] - nums[i + 1]
        return total
