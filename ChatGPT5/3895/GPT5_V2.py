"""Solution for counting occurrences of a digit in a list of integers."""


class Solution:  # pylint: disable=too-few-public-methods
    """Provide a solution for counting digit occurrences."""

    def countDigitOccurrences(self, nums, digit):  # pylint: disable=invalid-name
        """
        Count how often a digit appears in all numbers.

        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        target_digit = str(digit)

        return sum(str(number).count(target_digit) for number in nums)
