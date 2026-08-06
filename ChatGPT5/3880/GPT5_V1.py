class Solution(object):
    def minAbsoluteDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_one = -1
        last_two = -1
        ans = float("inf")

        for i, num in enumerate(nums):
            if num == 1:
                last_one = i
                if last_two != -1:
                    ans = min(ans, abs(last_one - last_two))
            elif num == 2:
                last_two = i
                if last_one != -1:
                    ans = min(ans, abs(last_one - last_two))

        return -1 if ans == float("inf") else ans
