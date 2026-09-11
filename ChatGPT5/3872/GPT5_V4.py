"""Find the longest arithmetic subarray after at most one replacement."""

# pylint: disable=too-few-public-methods


class Solution(object):
    """Solve the longest arithmetic subarray problem."""

    # pylint: disable=invalid-name
    def longestArithmetic(self, nums):
        """
        Return the maximum length of an arithmetic subarray.

        At most one element of nums may be replaced by any integer.

        :param nums: List of integers.
        :return: Maximum possible length of an arithmetic subarray.
        """
        n = len(nums)

        if n <= 2:
            return n

        left_length, left_diff = self._build_left_info(nums)
        right_length, right_diff = self._build_right_info(nums)

        best = max(left_length)

        # The replaced element can be the first or last element.
        best = max(best, right_length[1] + 1)
        best = max(best, left_length[n - 2] + 1)

        # Try replacing every element in the middle.
        for index in range(1, n - 1):
            best = max(
                best,
                self._extend_left(left_length, index),
                self._extend_right(right_length, index),
                self._bridge(
                    nums,
                    index,
                    left_length,
                    left_diff,
                    right_length,
                    right_diff,
                ),
            )

        return min(best, n)

    @staticmethod
    def _build_left_info(nums):
        """Build arithmetic run information from the left."""
        n = len(nums)
        lengths = [1] * n
        differences = [None] * n

        lengths[1] = 2
        differences[1] = nums[1] - nums[0]

        for index in range(2, n):
            difference = nums[index] - nums[index - 1]

            if difference == differences[index - 1]:
                lengths[index] = lengths[index - 1] + 1
            else:
                lengths[index] = 2

            differences[index] = difference

        return lengths, differences

    @staticmethod
    def _build_right_info(nums):
        """Build arithmetic run information from the right."""
        n = len(nums)
        lengths = [1] * n
        differences = [None] * n

        lengths[n - 2] = 2
        differences[n - 2] = nums[n - 1] - nums[n - 2]

        for index in range(n - 3, -1, -1):
            difference = nums[index + 1] - nums[index]

            if difference == differences[index + 1]:
                lengths[index] = lengths[index + 1] + 1
            else:
                lengths[index] = 2

            differences[index] = difference

        return lengths, differences

    @staticmethod
    def _extend_left(lengths, index):
        """Extend the arithmetic run on the left."""
        return lengths[index - 1] + 1

    @staticmethod
    def _extend_right(lengths, index):
        """Extend the arithmetic run on the right."""
        return lengths[index + 1] + 1

    @staticmethod
    def _bridge(
        nums,
        index,
        left_length,
        left_diff,
        right_length,
        right_diff,
    ):
        """Check whether the replaced element can connect both sides."""
        distance = nums[index + 1] - nums[index - 1]

        # The required difference must be an integer.
        if distance % 2 != 0:
            return 0

        difference = distance // 2

        left_matches = (
            index == 1 or left_diff[index - 1] == difference
        )
        right_matches = (
            index == len(nums) - 2
            or right_diff[index + 1] == difference
        )

        if not (left_matches and right_matches):
            return 0

        return (
            left_length[index - 1]
            + 1
            + right_length[index + 1]
        )
