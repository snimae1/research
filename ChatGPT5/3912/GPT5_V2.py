"""Find all elements that are valid according to the given conditions."""


class Solution(object):
    """Solution for finding valid elements in an integer array."""

    # pylint: disable=too-few-public-methods

    def findValidElements(self, nums):
        """
        Return all elements that are greater than every element
        on their left or on their right.

        :param nums: List of integers.
        :return: List of valid integers.
        """
        n = len(nums)

        # Store the largest value to the left of each position.
        left_max = [nums[0]] * n

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i])

        # Store the largest value to the right of each position.
        right_max = [nums[-1]] * n

        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])

        result = []

        for i in range(n):
            # The first and last elements are always valid.
            if i in (0, n - 1):
                result.append(nums[i])
                continue

            # An element is valid if it is strictly greater than
            # every element on its left or every element on its right.
            greater_than_left = nums[i] > left_max[i - 1]
            greater_than_right = nums[i] > right_max[i + 1]

            if greater_than_left or greater_than_right:
                result.append(nums[i])

        return result
