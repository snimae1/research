class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        
        # prefix_max[i] = max(nums[0..i])
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])
        
        # suffix_min[i] = min(nums[i..n-1])
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])
        
        # Find the smallest index with instability score <= k
        for i in range(n):
            if prefix_max[i] - suffix_min[i] <= k:
                return i
        
        return -1
