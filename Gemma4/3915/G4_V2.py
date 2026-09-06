"""
Module for calculating the maximum alternating sum of a subsequence
with a minimum distance constraint between indices.
"""

class FenwickTree:
    """
    Binary Indexed Tree (Fenwick Tree) to maintain prefix maximums.
    """
    def __init__(self, size):
        """Initializes the tree with a given size."""
        self.tree = [0] * (size + 1)

    def update(self, i, val):
        """Updates the value at index i to be the max of current and new val."""
        while i < len(self.tree):
            self.tree[i] = max(self.tree[i], val)
            i += i & (-i)

    def query(self, i):
        """Returns the maximum value in the range [1, i]."""
        res = 0
        while i > 0:
            res = max(res, self.tree[i])
            i -= i & (-i)
        return res


class Solution:
    """
    Provides a solution to find the maximum alternating sum of a subsequence.
    """

    def maxAlternatingSum(self, nums, k):
        """
        Calculates the max score of a strictly alternating subsequence 
        where each chosen index is at least k distance apart.
        
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0

        # Coordinate Compression: Map values to ranks [1...unique_count]
        # This allows the Fenwick Tree to operate on a dense range of indices.
        unique_sorted = sorted(list(set(nums)))
        rank_map = {val: i + 1 for i, val in enumerate(unique_sorted)}
        unique_count = len(unique_sorted)

        # bit_down: tracks max sums ending in a valley (to be followed by a peak)
        bit_down = FenwickTree(unique_count)
        # bit_up: tracks max sums ending in a peak (to be followed by a valley)
        # We use mirrored indexing (unique_count - rank + 1) to perform suffix queries.
        bit_up = FenwickTree(unique_count)

        n = len(nums)
        dp_up = [0] * n
        dp_down = [0] * n
        max_score = 0

        for i in range(n):
            # The distance condition: current index i can build upon index j = i - k
            j = i - k
            if j >= 0:
                val_j = nums[j]
                r_j = rank_map[val_j]
                bit_down.update(r_j, dp_down[j])
                bit_up.update(unique_count - r_j + 1, dp_up[j])

            curr_val = nums[i]
            curr_rank = rank_map[curr_val]

            # Case 1: Current element is a Peak.
            # We need a previous element (valley) that was strictly smaller.
            best_prev_down = bit_down.query(curr_rank - 1)
            dp_up[i] = max(curr_val, best_prev_down + curr_val)

            # Case 2: Current element is a Valley.
            # We need a previous element (peak) that was strictly larger.
            # Suffix query on [curr_rank + 1, unique_count] via mirrored BIT.
            best_prev_up = bit_up.query(unique_count - curr_rank)
            dp_down[i] = max(curr_val, best_prev_up + curr_val)

            max_score = max(max_score, dp_up[i], dp_down[i])

        return max_score
