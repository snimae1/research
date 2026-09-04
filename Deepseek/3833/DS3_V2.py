"""
Module for counting dominant indices in an array.
"""

class Solution:  # pylint: disable=too-few-public-methods
    """
    Provides a method to count indices where the element is greater than
    the average of all elements to its right.
    """

    def dominantIndices(self, nums):
        # pylint: disable=invalid-name
        """
        Count the number of dominant indices.

        A dominant index i satisfies:
            nums[i] > average(nums[i+1:])

        The rightmost element is never dominant.

        Args:
            nums (List[int]): List of integers.

        Returns:
            int: Number of dominant indices.
        """
        n = len(nums)
        count = 0
        # Iterate over all indices except the last one.
        for i in range(n - 1):
            # Compute sum of elements to the right.
            right_sum = sum(nums[i+1:])
            right_count = n - i - 1
            # Avoid floating-point comparison by cross-multiplying.
            # Condition: nums[i] > right_sum / right_count
            # Equivalent to: nums[i] * right_count > right_sum
            if nums[i] * right_count > right_sum:
                count += 1
        return count
