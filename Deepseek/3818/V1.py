class Solution(object):
    def minimumPrefixLength(self, nums):
        """
        Returns the minimum length of a prefix to remove so that the remaining
        suffix is strictly increasing.
        """
        n = len(nums)
        # Start from the end and find the longest strictly increasing suffix.
        start = n - 1
        while start > 0 and nums[start - 1] < nums[start]:
            start -= 1
        # The prefix to remove consists of all elements before 'start'.
        return start
