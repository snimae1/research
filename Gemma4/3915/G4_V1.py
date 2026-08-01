class Solution(object):
    def maxAlternatingSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        
        # Every decrease nums[i] > nums[i+1] requires at least this much
        # increase on the right side. These required increases can be done
        # independently, and a single operation can cover all elements to
        # the right of a drop.
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                ans += nums[i] - nums[i + 1]
        
        return ans
