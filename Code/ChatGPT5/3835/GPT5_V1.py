from collections import deque

class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxDeque = deque()  # monotonically decreasing
        minDeque = deque()  # monotonically increasing

        left = 0
        ans = 0

        for right in range(len(nums)):
            while maxDeque and nums[maxDeque[-1]] <= nums[right]:
                maxDeque.pop()
            maxDeque.append(right)

            while minDeque and nums[minDeque[-1]] >= nums[right]:
                minDeque.pop()
            minDeque.append(right)

            while (nums[maxDeque[0]] - nums[minDeque[0]]) * (right - left + 1) > k:
                if maxDeque[0] == left:
                    maxDeque.popleft()
                if minDeque[0] == left:
                    minDeque.popleft()
                left += 1

            ans += right - left + 1

        return ans
