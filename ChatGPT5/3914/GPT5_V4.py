"""Solution for making an array non-decreasing with minimum operations."""


class Solution(object):
    """Provide the solution for the minimum-operations problem."""

    def minOperations(self, nums):
        """
        Calculate the minimum sum of operation values.

        :type nums: List[int]
        :rtype: int
        """
        total = 0

        # A decrease must be compensated by increasing the current
        # element and possibly the elements that follow it.
        for index in range(1, len(nums)):
            if nums[index] < nums[index - 1]:
                total += nums[index - 1] - nums[index]

        return total
