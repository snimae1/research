"""
This module provides a solution to identify valid elements in an integer array
based on their relative values to elements on their left and right.
"""

class Solution:
    """
    A class containing the logic to solve the valid elements problem.
    """

    # pylint: disable=too-few-public-methods
    def find_valid_elements(self, nums):
        """
        Identifies elements that are strictly greater than all elements to their
        left or strictly greater than all elements to their right.

        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [nums[0]]

        # Boolean list to mark valid elements.
        # The first and last elements are always valid.
        is_valid = [False] * n
        is_valid[0] = True
        is_valid[n - 1] = True

        # Condition 1: Strictly greater than every element to its left.
        current_max_left = nums[0]
        for i in range(1, n):
            if nums[i] > current_max_left:
                is_valid[i] = True
                current_max_left = nums[i]

        # Condition 2: Strictly greater than every element to its right.
        current_max_right = nums[n - 1]
        for i in range(n - 2, -1, -1):
            if nums[i] > current_max_right:
                is_valid[i] = True
                current_max_right = nums[i]

        # Create result list based on the markings in is_valid.
        return [nums[i] for i in range(n) if is_valid[i]]
