"""Solution for maximizing the value of concatenated binary segments."""

from functools import cmp_to_key


class Solution(object):
    """Solve the maximum binary concatenation problem."""

    # pylint: disable=invalid-name,too-few-public-methods

    def maxValue(self, nums1, nums0):
        """
        Return the maximum possible value of the concatenated binary segments.

        :type nums1: List[int]
        :type nums0: List[int]
        :rtype: int
        """
        modulo = 1_000_000_007
        segments = list(zip(nums1, nums0))

        def compare_segments(first, second):
            """Determine the better order for two segments."""
            first_ones, first_zeros = first
            second_ones, second_zeros = second

            left = first_ones * second_zeros
            right = second_ones * first_zeros

            if left > right:
                return -1
            if left < right:
                return 1
            return 0

        segments.sort(key=cmp_to_key(compare_segments))

        result = 0

        for ones, zeros in segments:
            # Append all ones.
            for _ in range(ones):
                result = (result * 2 + 1) % modulo

            # Append all zeros.
            for _ in range(zeros):
                result = (result * 2) % modulo

        return result
