"""
Solution for finding the first stable index in an array.
"""

class Solution(object):
    """
    Class containing method to find first stable index.
    """
    # pylint: disable=too-few-public-methods

    def firstStableIndex(self, nums, k):
        """
        Find the smallest index i such that max(nums[0..i]) - min(nums[i..n-1]) <= k.

        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pylint: disable=invalid-name
        n = len(nums)

        # prefix_max[i] stores the maximum value from index 0 to i
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])

        # suffix_min[i] stores the minimum value from index i to n-1
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        # Iterate from left to right to find the first stable index
        for i in range(n):
            if prefix_max[i] - suffix_min[i] <= k:
                return i

        return -1
