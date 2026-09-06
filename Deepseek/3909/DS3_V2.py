"""
Module for comparing the sums of ascending and descending parts of a bitonic array.
"""

class Solution(object):
    """
    Provides a method to compare the sums of the two parts of a bitonic array.
    """

    def compareBitonicSums(self, nums):
        """
        Given a bitonic array, find the peak and compare the sum of the
        ascending part (including the peak) with the descending part (including the peak).

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        asc_sum = 0

        # Sum all elements before the peak (strictly increasing part)
        while i + 1 < n and nums[i] < nums[i + 1]:
            asc_sum += nums[i]
            i += 1

        peak = nums[i]
        asc_sum += peak  # include the peak in the ascending sum

        # Sum the peak and all elements after it (descending part)
        desc_sum = peak
        for j in range(i + 1, n):
            desc_sum += nums[j]

        # Compare the two sums and return the required result
        if asc_sum > desc_sum:
            return 0
        if desc_sum > asc_sum:
            return 1
        return -1
