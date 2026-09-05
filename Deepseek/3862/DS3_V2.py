"""
Solution for the "Smallest Balanced Index" problem.

This module contains the Solution class with a method to find the
smallest index i such that the sum of elements strictly to the left
equals the product of elements strictly to the right.
"""


class Solution:
    """
    Provides a method to compute the smallest balanced index in an array.
    """

    # The method name is intentionally left in PascalCase because it is
    # required by the problem statement.
    def smallestBalancedIndex(self, nums):  # pylint: disable=invalid-name
        """
        Return the smallest index i where the sum of elements left of i
        equals the product of elements right of i. If none exists, return -1.

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = sum(nums)

        # If the product on the right ever exceeds total_sum, it can never
        # equal any left sum (which is at most total_sum). We cap the product
        # to total_sum + 1 to avoid overflow and speed up calculations.
        product_cap = total_sum + 1

        # right_product[i] stores the product of nums[i:] capped at product_cap.
        right_product = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            prod = nums[i] * right_product[i + 1]
            right_product[i] = product_cap if prod > product_cap else prod

        left_sum = 0
        for i in range(n):
            # Product strictly to the right of index i is right_product[i + 1].
            if left_sum == right_product[i + 1]:
                return i
            left_sum += nums[i]

        return -1
