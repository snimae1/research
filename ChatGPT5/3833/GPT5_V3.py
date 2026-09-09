"""Solution for counting dominant indices in an integer array."""


class Solution(object):
    """Provide a solution for counting dominant indices."""

    # Pylint naming conventions are intentionally disabled because the
    # online judge requires this exact method name.
    # pylint: disable=invalid-name,too-few-public-methods

    def dominantIndices(self, nums):
        """
        Count indices whose value is greater than the average of all
        elements to their right.

        :type nums: List[int]
        :rtype: int
        """
        array_length = len(nums)

        if array_length <= 1:
            return 0

        right_sum = sum(nums)
        dominant_count = 0

        for index in range(array_length - 1):
            right_sum -= nums[index]
            right_count = array_length - index - 1

            # Avoid floating-point arithmetic when comparing with the average.
            if nums[index] * right_count > right_sum:
                dominant_count += 1

        return dominant_count
