"""Solution for finding the smallest balanced index in an integer array."""


class Solution:  # pylint: disable=too-few-public-methods
    """Provide a solution for finding the smallest balanced index."""

    def smallestBalancedIndex(self, nums):  # pylint: disable=invalid-name
        """
        Return the smallest index where the left sum equals the right product.

        :type nums: List[int]
        :rtype: int
        """
        right_product = 1

        for number in nums:
            right_product *= number

        left_sum = 0

        for index, number in enumerate(nums):
            right_product //= number

            if left_sum == right_product:
                return index

            left_sum += number

        return -1
