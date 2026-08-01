from typing import List

class Solution(object):
    def countGoodSubarrays(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        MAX_BITS = 30  # 10^9 < 2^30

        # prev_non_subset[i] = largest index j < i with (nums[j] & ~nums[i]) != 0, else -1
        prev_non_subset = []
        # prev_equal[i] = largest index j < i with nums[j] == nums[i], else -1
        prev_equal = []

        last_bit = [-1] * MAX_BITS
        last_val = {}

        for i, x in enumerate(nums):
            # max last occurrence of any bit that is NOT set in x
            max_last = -1
            for b in range(MAX_BITS):
                if (x >> b) & 1 == 0:
                    if last_bit[b] > max_last:
                        max_last = last_bit[b]
            prev_non_subset.append(max_last)

            pe = last_val.get(x, -1)
            prev_equal.append(pe)
            last_val[x] = i

            # update last_bit for bits set in x
            for b in range(MAX_BITS):
                if (x >> b) & 1:
                    last_bit[b] = i

        # right_non_subset[i] = smallest index j > i with (nums[j] & ~nums[i]) != 0, else n
        right_non_subset = [0] * n
        next_bit = [n] * MAX_BITS

        for i in range(n - 1, -1, -1):
            x = nums[i]
            min_next = n
            for b in range(MAX_BITS):
                if (x >> b) & 1 == 0:
                    if next_bit[b] < min_next:
                        min_next = next_bit[b]
            right_non_subset[i] = min_next

            # update next_bit for bits set in x
            for b in range(MAX_BITS):
                if (x >> b) & 1:
                    next_bit[b] = i

        ans = 0
        for i in range(n):
            left_min = max(prev_non_subset[i], prev_equal[i]) + 1
            right_max = right_non_subset[i] - 1
            # number of choices for left boundary L and right boundary R
            ans += (i - left_min + 1) * (right_max - i + 1)

        return ans
