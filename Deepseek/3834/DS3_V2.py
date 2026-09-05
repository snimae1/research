# pylint: disable=invalid-name, useless-object-inheritance, too-few-public-methods
"""
Module for merging adjacent equal elements in an array.
"""

class Solution(object):
    """
    Provides a method to merge adjacent equal elements repeatedly.
    """

    def mergeAdjacent(self, nums):
        """
        Merge adjacent equal elements in the array.

        Given an integer array, repeatedly merge the leftmost adjacent equal pair
        by replacing them with their sum, until no adjacent equal elements remain.

        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        for x in nums:
            # While the current value equals the top of the stack,
            # merge them by adding the top to x and removing it.
            while stack and stack[-1] == x:
                x += stack.pop()
            stack.append(x)
        return stack
