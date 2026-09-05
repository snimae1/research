"""
Module to determine if an array can be transformed into a uniform parity array.
"""

class Solution:
    """
    Provides a method to check if an array can be made uniform (all even or all odd)
    by subtracting elements.
    """

    def uniformArray(self, nums1):
        """
        Check if it is possible to construct an array where all elements are
        either all odd or all even.

        :type nums1: List[int]
        :rtype: bool
        """ 
        # Find the smallest element. It cannot be changed via subtraction
        # because no other index j exists such that nums1[i] - nums1[j] >= 1.
        min_val = min(nums1)

        # Case A: The minimum element is odd.
        # We can make all elements odd:
        # - Odd numbers remain odd.
        # - Even numbers E become (E - min_val), which is always odd.
        if min_val % 2 != 0:
            return True

        # Case B: The minimum element is even.
        # Since the minimum cannot be changed, all elements must be even.
        # An odd number could only become even if we subtract another odd number.
        # However, if the absolute minimum is even, the smallest odd number
        # cannot be made even because there is no smaller odd number available.
        for num in nums1:
            if num % 2 != 0:
                return False
        
        return True
