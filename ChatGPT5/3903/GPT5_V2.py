"""Solution for finding the first stable index in an integer array."""


class Solution:
    """Provide a method for finding the first stable index."""

    def firstStableIndex(self, nums, k):  # pylint: disable=invalid-name
        """
        Return the first index whose instability score is at most k.

        The instability score at index i is the difference between
        the maximum value in nums[0..i] and the minimum value in
        nums[i..n-1].

        :param nums: List of integers.
        :param k: Maximum allowed instability score.
        :return: The smallest stable index, or -1 if none exists.
        """
        n = len(nums)

        # Build an array containing the minimum value from each index
        # to the end of the array.
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]

        for index in range(n - 2, -1, -1):
            suffix_min[index] = min(nums[index], suffix_min[index + 1])

        # Track the maximum value from the beginning up to the
        # current index and check each index from left to right.
        prefix_max = nums[0]

        for index in range(n):
            prefix_max = max(prefix_max, nums[index])

            instability_score = prefix_max - suffix_min[index]

            if instability_score <= k:
                return index

        return -1
