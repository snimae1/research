"""
This module provides a solution for merging adjacent equal elements in an integer array.
The merging process continues until no two adjacent elements are equal.
"""

class Solution:
    """
    A class to handle the logic of merging adjacent equal elements.
    """

    def merge_adjacent(self, nums):
        """
        Repeatedly merge the leftmost pair of equal adjacent elements into their sum.

        :type nums: List[int]
        :rtype: List[int]
        """
        # A stack is used to efficiently handle merges from left to right.
        # This ensures the 'leftmost' requirement and provides O(n) complexity.
        stack = []

        for num in nums:
            current_val = num

            # Check if the current element can be merged with the top of the stack.
            # We use a while loop because a merge might trigger further merges
            # with the preceding elements in the stack.
            while stack and stack[-1] == current_val:
                current_val += stack.pop()

            stack.append(current_val)

        return stack
