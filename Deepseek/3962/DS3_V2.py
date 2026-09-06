"""Solution for LeetCode problem: Maximum Subarray Sum with Swaps."""


class Fenwick:
    """Fenwick tree to maintain counts and sums of ranks efficiently."""

    def __init__(self, size, values_by_rank):
        self.size = size
        self.values_by_rank = values_by_rank
        self.tree_count = [0] * (size + 1)
        self.tree_sum = [0] * (size + 1)
        self.total_count = 0
        self.total_sum = 0
        self.highest_bit = 1 << (size.bit_length() - 1)

    def add(self, idx, d_cnt, d_sum):
        """Add d_cnt and d_sum at rank idx (1-based)."""
        self.total_count += d_cnt
        self.total_sum += d_sum
        while idx <= self.size:
            self.tree_count[idx] += d_cnt
            self.tree_sum[idx] += d_sum
            idx += idx & -idx

    def prefix_count(self, idx):
        """Count of elements with rank <= idx."""
        res = 0
        while idx > 0:
            res += self.tree_count[idx]
            idx -= idx & -idx
        return res

    def prefix_sum(self, idx):
        """Sum of elements with rank <= idx."""
        res = 0
        while idx > 0:
            res += self.tree_sum[idx]
            idx -= idx & -idx
        return res

    def kth(self, k_val):
        """Find the rank of the k-th smallest element (1-indexed)."""
        idx = 0
        bit = self.highest_bit
        while bit:
            nxt = idx + bit
            if nxt <= self.size and self.tree_count[nxt] < k_val:
                k_val -= self.tree_count[nxt]
                idx = nxt
            bit >>= 1
        return idx + 1

    def sum_smallest(self, x):
        """Return the sum of the x smallest elements."""
        if x <= 0:
            return 0
        rank = self.kth(x)
        cnt_before = self.prefix_count(rank - 1)
        sum_before = self.prefix_sum(rank - 1)
        value = self.values_by_rank[rank]
        return sum_before + (x - cnt_before) * value


class Solution:
    """Solve the problem using two Fenwick trees for efficient swap calculation."""

    def _max_sum_no_swaps(self, nums):
        """Kadane's algorithm for maximum subarray sum without any swaps."""
        max_ending = max_so_far = nums[0]
        for x in nums[1:]:
            max_ending = max(x, max_ending + x)
            max_so_far = max(max_so_far, max_ending)
        return max_so_far

    def _optimal_swaps(self, inside, outside, k):
        """
        Determine the optimal number of beneficial swaps between inside and outside.

        A swap is beneficial if we replace a smaller element from inside by a
        larger element from outside. The maximum number of such swaps is limited by
        k and the counts of both sets.
        """
        max_x = min(k, inside.total_count, outside.total_count)
        if max_x == 0:
            return 0

        # Binary search for the largest rank r where outside_ge(r) >= inside_le(r)
        lo, hi = 1, inside.size
        best_r = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            in_le = inside.prefix_count(mid)
            out_ge = outside.total_count - outside.prefix_count(mid - 1)
            if out_ge >= in_le:
                best_r = mid
                lo = mid + 1
            else:
                hi = mid - 1

        if best_r == -1:
            # No rank satisfies the condition; maximum at r = 1
            out_ge1 = outside.total_count
            in_le1 = inside.prefix_count(1)
            ans_x = min(out_ge1, in_le1)
        else:
            out_ge_r = outside.total_count - outside.prefix_count(best_r - 1)
            in_le_r = inside.prefix_count(best_r)
            cand1 = min(out_ge_r, in_le_r)
            if best_r < inside.size:
                out_ge_r1 = outside.total_count - outside.prefix_count(best_r)
                in_le_r1 = inside.prefix_count(best_r + 1)
                cand2 = min(out_ge_r1, in_le_r1)
                ans_x = max(cand1, cand2)
            else:
                ans_x = cand1

        return min(ans_x, max_x)

    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        # Special cases
        if k == 0:
            return self._max_sum_no_swaps(nums)

        if k >= n:
            # We can rearrange almost the whole array – take all positives
            pos_sum = sum(x for x in nums if x > 0)
            return pos_sum if pos_sum > 0 else max(nums)

        # Coordinate compression
        uniq = sorted(set(nums))
        size = len(uniq)
        rank_of_value = {v: i + 1 for i, v in enumerate(uniq)}
        values_by_rank = [0] + uniq  # 1-indexed

        total_all_sum = sum(nums)

        outside = Fenwick(size, values_by_rank)
        for val in nums:
            outside.add(rank_of_value[val], 1, val)

        max_ans = -10**18

        for i in range(n):
            inside = Fenwick(size, values_by_rank)
            for j in range(i, n):
                val = nums[j]
                rank = rank_of_value[val]

                # Move current element from outside to inside
                inside.add(rank, 1, val)
                outside.add(rank, -1, -val)

                # Calculate optimal swaps for this subarray
                opt_x = self._optimal_swaps(inside, outside, k)

                if opt_x > 0:
                    sum_in_small = inside.sum_smallest(opt_x)
                    sum_out_large = outside.total_sum - outside.sum_smallest(
                        outside.total_count - opt_x
                    )
                    boost = sum_out_large - sum_in_small
                else:
                    boost = 0

                cur = inside.total_sum + boost
                max_ans = max(max_ans, cur)

        return max_ans
