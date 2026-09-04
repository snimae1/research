"""
This module provides a solution to find the maximum length of an alternating
subarray after potentially removing one element from the input list.
"""

# pylint: disable=too-few-public-methods
class Solution:
    """
    Contains the logic to calculate the longest alternating subarray.
    """

    # pylint: disable=invalid-name
    def longestAlternating(self, nums):
        """
        Finds the maximum length of an alternating subarray where comparisons
        between adjacent elements alternate between strictly greater and strictly smaller.
        One element can be optionally removed to maximize this length.

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n

        # left_asc[i]: length of alternating subarray ending at i with an increase (nums[i-1] < nums[i])
        # left_desc[i]: length of alternating subarray ending at i with a decrease (nums[i-1] > nums[i])
        left_asc = [1] * n
        left_desc = [1] * n

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                left_asc[i] = left_desc[i - 1] + 1
            elif nums[i] < nums[i - 1]:
                left_desc[i] = left_asc[i - 1] + 1

        # right_asc[i]: length of alternating subarray starting at i with an increase (nums[i] < nums[i+1])
        # right_desc[i]: length of alternating subarray starting at i with a decrease (nums[i] > nums[i+1])
        right_asc = [1] * n
        right_desc = [1] * n

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                right_asc[i] = right_desc[i + 1] + 1
            elif nums[i] > nums[i + 1]:
                right_desc[i] = right_asc[i + 1] + 1

        # Calculate maximum length without removing any element
        max_len = 0
        for i in range(n):
            current_max = max(left_asc[i], left_desc[i])
            if current_max > max_len:
                max_len = current_max

        # Try removing one element at index i to bridge two alternating subarrays
        for i in range(1, n - 1):
            prev_idx = i - 1
            next_idx = i + 1

            if nums[prev_idx] < nums[next_idx]:
                # Bridge is an increase (<).
                # Needs a subarray ending in decrease on left and starting with decrease on right.
                combined_len = left_desc[prev_idx] + right_desc[next_idx]
                if combined_len > max_len:
                    max_len = combined_len
            elif nums[prev_idx] > nums[next_idx]:
                # Bridge is a decrease (>).
                # Needs a subarray ending in increase on left and starting with increase on right.
                combined_len = left_asc[prev_idx] + right_asc[next_idx]
                if combined_len > max_len:
                    max_len = combined_len

        return max_len
