class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        
        # Every time an element is smaller than the previous one,
        # we must increase this element (and possibly following ones)
        # by at least the difference.
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                ans += nums[i - 1] - nums[i]
        
        return ans
