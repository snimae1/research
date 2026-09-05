# pylint: disable=invalid-name, too-few-public-methods
"""Solution for LeetCode problem 3876DS3."""

class Solution:
    """Class containing method to check uniform array possibility."""
    
    def uniformArray(self, nums1):
        """
        Check if it is possible to construct nums2 with uniform parity.

        :type nums1: List[int]
        :rtype: bool
        """
        # If all numbers are even, we can keep them as they are.
        all_even = all(x % 2 == 0 for x in nums1)
        # If the smallest number is odd, every even number can be transformed
        # into an odd number by subtracting the odd minimum.
        min_val = min(nums1)
        return all_even or (min_val % 2 == 1)
