class Solution(object):
    def minAbsoluteDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last1 = -1
        last2 = -1
        min_diff = float('inf')

        for i, num in enumerate(nums):
            if num == 1:
                if last2 != -1:
                    min_diff = min(min_diff, i - last2)
                last1 = i
            elif num == 2:
                if last1 != -1:
                    min_diff = min(min_diff, i - last1)
                last2 = i

        return min_diff if min_diff != float('inf') else -1
