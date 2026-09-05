"""
Solution for the "Make Parity Alternating" problem.
"""

# pylint: disable=invalid-name, too-few-public-methods

class Solution:
    """
    Provides a method to transform an array into a parity alternating array
    with minimum operations and compute the minimum possible value range.
    """

    def makeParityAlternating(self, nums):
        """
        Computes the minimum operations to make the array parity alternating,
        and the minimum possible value of max(nums) - min(nums) after exactly
        that many operations.

        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return [0, 0]

        # Count mismatches for the two parity patterns:
        # pattern 0: even at even indices, odd at odd indices
        # pattern 1: odd at even indices, even at odd indices
        mismatches = [0, 0]
        for i, num in enumerate(nums):
            parity = num % 2
            for p in (0, 1):
                desired = (i % 2) ^ p
                if parity != desired:
                    mismatches[p] += 1

        min_ops = min(mismatches)

        # Find the best (minimum) range among patterns that achieve min_ops
        best_range = float('inf')
        for p in (0, 1):
            if mismatches[p] == min_ops:
                best_range = min(best_range, self._min_range_for_pattern(nums, p))

        return [min_ops, int(best_range)]

    def _min_range_for_pattern(self, nums, pattern):
        """
        For a given parity pattern, compute the minimum possible range
        after applying exactly the necessary number of +/-1 operations.
        """
        fixed = []
        free = []
        for i, num in enumerate(nums):
            desired = (i % 2) ^ pattern
            if num % 2 == desired:
                fixed.append(num)
            else:
                free.append(num)

        if not free:
            if not fixed:
                return 0
            return max(fixed) - min(fixed)

        # Sort both lists to efficiently compute prefix/suffix extrema.
        fixed.sort()
        free.sort()
        m = len(free)

        # Prefix extrema for free elements that will be increased by 1.
        pref_max_plus = [float('-inf')] * m
        pref_min_plus = [float('inf')] * m
        pref_max_plus[0] = free[0] + 1
        pref_min_plus[0] = free[0] + 1
        for i in range(1, m):
            pref_max_plus[i] = max(pref_max_plus[i - 1], free[i] + 1)
            pref_min_plus[i] = min(pref_min_plus[i - 1], free[i] + 1)

        # Suffix extrema for free elements that will be decreased by 1.
        suff_max_minus = [float('-inf')] * m
        suff_min_minus = [float('inf')] * m
        suff_max_minus[m - 1] = free[m - 1] - 1
        suff_min_minus[m - 1] = free[m - 1] - 1
        for i in range(m - 2, -1, -1):
            suff_max_minus[i] = max(suff_max_minus[i + 1], free[i] - 1)
            suff_min_minus[i] = min(suff_min_minus[i + 1], free[i] - 1)

        max_fixed = max(fixed) if fixed else float('-inf')
        min_fixed = min(fixed) if fixed else float('inf')

        best_range = float('inf')
        # p = number of free elements that receive +1 (the rest receive -1)
        for p in range(m + 1):
            cur_max = max_fixed
            cur_min = min_fixed
            if p > 0:
                cur_max = max(cur_max, pref_max_plus[p - 1])
                cur_min = min(cur_min, pref_min_plus[p - 1])
            if p < m:
                cur_max = max(cur_max, suff_max_minus[p])
                cur_min = min(cur_min, suff_min_minus[p])
            best_range = min(best_range, cur_max - cur_min)

        return best_range
