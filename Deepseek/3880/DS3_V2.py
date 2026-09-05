"""Solution for finding minimum absolute difference between indices of 1 and 2."""

class Solution(object):
    """Contains method to compute minimum absolute difference."""
    def minAbsoluteDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize last seen positions of 1 and 2 as -1 (not seen yet)
        last_one = -1
        last_two = -1
        min_diff = float('inf')

        for i, num in enumerate(nums):
            if num == 1:
                # If we have seen a 2 before, update min_diff with current distance
                if last_two != -1:
                    min_diff = min(min_diff, i - last_two)
                last_one = i
            elif num == 2:
                # If we have seen a 1 before, update min_diff with current distance
                if last_one != -1:
                    min_diff = min(min_diff, i - last_one)
                last_two = i

        # Return -1 if no valid pair found
        return min_diff if min_diff != float('inf') else -1
