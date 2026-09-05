"""
Module for determining if a uniform array can be constructed.
"""

# pylint: disable=invalid-name
class Solution:
    """
    Solution class for the uniform array problem.
    """

    # pylint: disable=too-few-public-methods
    def uniformArray(self, nums1):
        """
        Check if it is possible to construct an array with all odd or all even elements.

        :type nums1: List[int]
        :rtype: bool
        """
        # It is always possible to construct such an array.
        # For any given distinct integers, we can always choose either
        # all even or all odd numbers by using the subtraction operation
        # appropriately. The only edge case is n=1, where we take the single
        # element as is, which trivially satisfies the condition.
        return True
