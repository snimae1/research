class Solution(object):
    def maxAlternatingSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        max_val = max(nums)

        # Fenwick tree (Binary Indexed Tree) for maximum queries
        class BIT:
            def __init__(self, size):
                self.n = size
                self.tree = [-10**18] * (size + 2)  # 1-indexed

            def update(self, idx, val):
                while idx <= self.n:
                    if val > self.tree[idx]:
                        self.tree[idx] = val
                    idx += idx & -idx

            def query(self, idx):
                res = -10**18
                while idx > 0:
                    if self.tree[idx] > res:
                        res = self.tree[idx]
                    idx -= idx & -idx
                return res

        # BIT for valleys: dp_valley values indexed by original value
        bit_valley = BIT(max_val)
        # BIT for peaks: dp_peak values indexed by reversed value
        bit_peak = BIT(max_val)

        dp_peak = [0] * n
        dp_valley = [0] * n
        ans = 0

        for i in range(n):
            # Add the element that is exactly k positions behind
            if i - k >= 0:
                v = nums[i - k]
                bit_valley.update(v, dp_valley[i - k])
                rev = max_val - v + 1
                bit_peak.update(rev, dp_peak[i - k])

            val = nums[i]

            # Best previous valley with value < val
            if val > 1:
                max_prev_valley = bit_valley.query(val - 1)
            else:
                max_prev_valley = -10**18

            # Best previous peak with value > val
            if val < max_val:
                # reversed index for values > val: query prefix up to max_val - val
                max_prev_peak = bit_peak.query(max_val - val)
            else:
                max_prev_peak = -10**18

            # Start a new subsequence with this element, or extend existing one
            dp_peak[i] = max(val, val + max_prev_valley)
            dp_valley[i] = max(val, val + max_prev_peak)

            ans = max(ans, dp_peak[i], dp_valley[i])

        return ans
