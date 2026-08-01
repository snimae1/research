class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        # Check if all numbers are even
        all_even = all(x % 2 == 0 for x in nums1)
        # Find the global minimum
        min_val = min(nums1)
        # Possible if all even or the smallest number is odd
        return all_even or (min_val % 2 == 1)
