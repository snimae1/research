"""
This module provides a solution to count the occurrences of a specific 
digit within a list of integers.
"""

class Solution:
    """
    A class to solve the digit counting problem.
    """

    def count_digit_occurrences(self, nums, digit):
        """
        Counts the total number of times a digit appears in 
        the decimal representation of all elements in the list.

        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        digit_str = str(digit)
        total_count = 0

        for num in nums:
            total_count += str(num).count(digit_str)

        return total_count
