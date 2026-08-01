from collections import deque

class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        max_dq = deque()  # stores indices, maintains decreasing values
        min_dq = deque()  # stores indices, maintains increasing values
        left = 0
        ans = 0

        for right in range(n):
            # Add nums[right] to the monotonic deques
            while max_dq and nums[max_dq[-1]] <= nums[right]:
                max_dq.pop()
            max_dq.append(right)

            while min_dq and nums[min_dq[-1]] >= nums[right]:
                min_dq.pop()
            min_dq.append(right)

            # Shrink window from left until the cost condition holds
            while left <= right:
                cur_max = nums[max_dq[0]]
                cur_min = nums[min_dq[0]]
                length = right - left + 1
                cost = (cur_max - cur_min) * length
                if cost <= k:
                    break
                # Remove nums[left] from deques if it is at the front
                if max_dq[0] == left:
                    max_dq.popleft()
                if min_dq[0] == left:
                    min_dq.popleft()
                left += 1

            # All subarrays ending at 'right' with start index >= left are valid
            ans += right - left + 1

        return ans
