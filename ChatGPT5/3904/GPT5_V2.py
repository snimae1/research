"""Find the first stable index in an integer array."""


class Solution:
    """Provide a solution for finding the first stable index."""

    def firstStableIndex(self, nums, k):
        """
        Find the smallest index with an instability score <= k.

        :param nums: List of integers.
        :param k: Maximum allowed instability score.
        :return: The smallest stable index, or -1 if none exists.
        """
        n = len(nums)

        # Store the minimum value from each index to the end of the array.
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        # Track the maximum value from the beginning up to the current index.
        prefix_max = nums[0]

        for i in range(n):
            prefix_max = max(prefix_max, nums[i])

            # The instability score is:
            # max(nums[0..i]) - min(nums[i..n-1]).
            instability_score = prefix_max - suffix_min[i]

            if instability_score <= k:
                return i

        return -1
