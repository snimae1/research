# pylint: disable=invalid-name, too-few-public-methods
"""
Solution for the problem "Maximum Alternating Subsequence Sum with Distance Constraint".

The task is to find the maximum possible sum of a subsequence that is strictly
alternating and satisfies a minimum index distance of k between consecutive
chosen elements.
"""

class Solution:
    """
    Provides the method to compute the maximum alternating sum with a distance constraint.
    """

    def maxAlternatingSum(self, nums, k):
        """
        Returns the maximum possible score of a valid alternating subsequence
        with index distance at least k.

        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        max_val = max(nums)

        # Negative infinity for initialization of Fenwick trees
        NEG_INF = -10**18

        class BIT:
            """
            Fenwick tree (Binary Indexed Tree) for prefix maximum queries.
            Supports point updates and range maximum queries over prefix.
            """

            def __init__(self, size):
                """
                Initializes the Fenwick tree with given size (1-indexed).
                All entries start at NEG_INF.
                """
                self.n = size
                self.tree = [NEG_INF] * (size + 2)

            def update(self, idx, val):
                """
                Updates position idx with the maximum of current value and val.
                """
                while idx <= self.n:
                    if val > self.tree[idx]:
                        self.tree[idx] = val
                    idx += idx & -idx

            def query(self, idx):
                """
                Returns the maximum value among indices 1..idx.
                """
                res = NEG_INF
                while idx > 0:
                    if self.tree[idx] > res:
                        res = self.tree[idx]
                    idx -= idx & -idx
                return res

        # Two Fenwick trees:
        # - bit_valley: stores best dp_valley values indexed by the numeric value
        #   (used to find best previous valley with value < current)
        # - bit_peak  : stores best dp_peak values indexed by reversed value
        #   (used to find best previous peak with value > current)
        bit_valley = BIT(max_val)
        bit_peak = BIT(max_val)

        # dp_peak[i]  : best score ending at i where nums[i] is a peak (increasing transition)
        # dp_valley[i]: best score ending at i where nums[i] is a valley (decreasing transition)
        dp_peak = [0] * n
        dp_valley = [0] * n
        ans = 0

        for i in range(n):
            # Add element that is exactly k positions behind into the BITs
            # This ensures that any query only considers indices j <= i - k
            if i - k >= 0:
                # update valley tree with value nums[i-k]
                bit_valley.update(nums[i - k], dp_valley[i - k])
                # update peak tree with reversed index
                bit_peak.update(max_val - nums[i - k] + 1, dp_peak[i - k])

            val = nums[i]

            # Best previous valley with value strictly less than val
            if val > 1:
                max_prev_valley = bit_valley.query(val - 1)
            else:
                max_prev_valley = NEG_INF

            # Best previous peak with value strictly greater than val
            if val < max_val:
                # reversed index for values > val: prefix up to max_val - val
                max_prev_peak = bit_peak.query(max_val - val)
            else:
                max_prev_peak = NEG_INF

            # Either start a new subsequence with this element alone,
            # or extend a previous alternating subsequence that ended with a valley/peak
            dp_peak[i] = max(val, val + max_prev_valley)
            dp_valley[i] = max(val, val + max_prev_peak)

            # Update overall answer
            if dp_peak[i] > ans:
                ans = dp_peak[i]
            if dp_valley[i] > ans:
                ans = dp_valley[i]

        return ans
