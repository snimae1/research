from typing import List

# Max bits needed since nums[i] <= 10^9 < 2^30
MAX_BITS = 30


class Solution:
    def countGoodSubarrays(self, nums: List[int]) -> int:
        """
        Counts subarrays where the bitwise OR of all elements equals at least one element.

        For each index i, we count subarrays where nums[i] is the leftmost occurrence
        of its value and all other elements are bitwise subsets of nums[i].
        In such a subarray, the OR equals nums[i], making it good.
        Duplicate counting is avoided by requiring leftmost occurrence of the value.
        """
        n = len(nums)

        # prev_non_subset[i] = largest j < i with (nums[j] & ~nums[i]) != 0, else -1
        prev_non_subset = [-1] * n
        # prev_equal[i] = largest j < i with nums[j] == nums[i], else -1
        prev_equal = [-1] * n

        last_bit = [-1] * MAX_BITS   # last index where each bit was set
        last_val = {}                # last index for each value

        # Forward pass: compute prev_non_subset and prev_equal
        for i, x in enumerate(nums):
            max_last = -1
            for b in range(MAX_BITS):
                if (x >> b) & 1:
                    last_bit[b] = i
                else:
                    if last_bit[b] > max_last:
                        max_last = last_bit[b]
            prev_non_subset[i] = max_last

            pe = last_val.get(x, -1)
            prev_equal[i] = pe
            last_val[x] = i

        ans = 0
        next_bit = [n] * MAX_BITS   # next index where each bit will be set (from right)

        # Backward pass: for each i, compute right limit and add contribution
        for i in range(n - 1, -1, -1):
            x = nums[i]
            min_next = n
            for b in range(MAX_BITS):
                if (x >> b) & 1:
                    next_bit[b] = i
                else:
                    if next_bit[b] < min_next:
                        min_next = next_bit[b]
            right_max = min_next - 1

            left_min = max(prev_non_subset[i], prev_equal[i]) + 1
            # Number of valid left boundaries times valid right boundaries
            ans += (i - left_min + 1) * (right_max - i + 1)

        return ans
