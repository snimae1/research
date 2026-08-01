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
        current_max = nums[0]
        for i in range(n):
            if nums[i] > current_max:
                current_max = nums[i]
            prefix_max[i] = current_max

        # suffix_min[i] = min(nums[i..n-1])
        suffix_min = [0] * n
        current_min = nums[-1]
        for i in range(n - 1, -1, -1):
            if nums[i] < current_min:
                current_min = nums[i]
            suffix_min[i] = current_min

        # Find smallest stable index
        for i in range(n):
            if prefix_max[i] - suffix_min[i] <= k:
                return i
        return -1
