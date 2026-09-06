"""Solution for counting digit occurrences in numbers."""
# pylint: disable=invalid-name, too-few-public-methods, useless-object-inheritance

class Solution(object):
    """Provides method to count occurrences of a digit in an array of integers."""
    def countDigitOccurrences(self, nums, digit):
        """
        Count total occurrences of a given digit in decimal representation of all numbers.

        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        total = 0
        target = str(digit)
        for num in nums:
            total += str(num).count(target)
        return total
