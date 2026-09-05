"""
Solution for counting subarrays where (max-min)*length <= k.
Uses sliding window with two monotonic deques to track max/min in O(n) time.
"""

from collections import deque

class Solution:  # Python 3, no need to inherit from object
    # pylint: disable=invalid-name
    def countSubarrays(self, nums, k):
        """
        Count the number of subarrays whose cost (max-min)*length <= k.

        :param nums: List[int] - input array
        :param k: int - maximum allowed cost
        :return: int - number of valid subarrays
        """
        n = len(nums)
        max_deque = deque()  # stores indices, values strictly decreasing
        min_deque = deque()  # stores indices, values strictly increasing
        left = 0
        ans = 0

        for right in range(n):
            # Maintain max_deque: remove smaller or equal values from back
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)

            # Maintain min_deque: remove larger or equal values from back
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)

            # Shrink window from the left until cost condition holds
            while left <= right:
                cur_max = nums[max_deque[0]]
                cur_min = nums[min_deque[0]]
                length = right - left + 1
                cost = (cur_max - cur_min) * length
                if cost <= k:
                    break
                # Remove left index from deques if it is at the front
                if max_deque[0] == left:
                    max_deque.popleft()
                if min_deque[0] == left:
                    min_deque.popleft()
                left += 1

            # All subarrays ending at 'right' with start >= left are valid
            ans += right - left + 1

        return ans
