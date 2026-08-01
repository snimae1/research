class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        # suffix_min[i] speichert das Minimum von nums[i..n-1]
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        # prefix_max während des Durchlaufens berechnen
        prefix_max = nums[0]

        for i in range(n):
            if nums[i] > prefix_max:
                prefix_max = nums[i]

            # Instability Score = max(nums[0..i]) - min(nums[i..n-1])
            if prefix_max - suffix_min[i] <= k:
                return i

        return -1
