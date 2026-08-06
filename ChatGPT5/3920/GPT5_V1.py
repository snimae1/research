class Solution(object):
    def maxFixedPoints(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        need = 0
        for x in nums:
            if x == need:
                need += 1
        return need
