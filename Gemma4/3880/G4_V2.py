"""
This module provides a solution to find the minimum absolute difference 
between the indices of elements 1 and 2 in a given list.
"""

class Solution:
    """
    A class containing the logic to calculate the minimum absolute difference
    between indices of valid pairs (1, 2).
    """

    def min_absolute_difference(self, nums):
        """
        Calculates the minimum absolute difference between indices i and j 
        where nums[i] == 1 and nums[j] == 2.

        :type nums: List[int]
        :rtype: int
        """
        # Initialize min_diff with infinity to easily find the minimum
        min_diff = float('inf')
        
        # Track the last seen index of 1 and 2
        last_one = -1
        last_two = -1

        # Using enumerate instead of range(len(nums)) for better Pythonic style
        for i, num in enumerate(nums):
            if num == 1:
                last_one = i
                # If a '2' was already found, calculate the distance
                if last_two != -1:
                    min_diff = min(min_diff, abs(i - last_two))
            
            elif num == 2:
                last_two = i
                # If a '1' was already found, calculate the distance
                if last_one != -1:
                    min_diff = min(min_diff, abs(i - last_one))

        # Return -1 if no valid pair was found, otherwise return the minimum difference
        return min_diff if min_diff != float('inf') else -1
