"""
Module for solving the minimum prefix length problem.
"""


class Solution:
    """
    Provides a method to compute the minimum prefix length to remove
    so that the remaining array is strictly increasing.
    """

    # pylint: disable=too-few-public-methods
    def minimumPrefixLength(self, nums):
        # pylint: disable=invalid-name
        """
        Returns the length of the shortest prefix to remove from `nums`
        such that the remaining suffix is strictly increasing.

        Args:
            nums (List[int]): The input integer array.

        Returns:
            int: The minimum length of the prefix to remove.
        """
        n = len(nums)
        # Start from the end and find the longest strictly increasing suffix.
        start = n - 1
        while start > 0 and nums[start - 1] < nums[start]:
            start -= 1
        # The prefix to remove consists of all elements before 'start'.
        return start
