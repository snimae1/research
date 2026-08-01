class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        # Suffix-Minimum berechnen:
        # suffix_min[i] = Minimum von nums[i..n-1]
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        # Prefix-Maximum laufend berechnen und prüfen
        prefix_max = nums[0]

        for i in range(n):
            if nums[i] > prefix_max:
                prefix_max = nums[i]

            # Instability Score = max(nums[0..i]) - min(nums[i..n-1])
            if prefix_max - suffix_min[i] <= k:
                return i

        return -1
