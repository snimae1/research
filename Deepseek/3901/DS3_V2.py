"""
Solution for counting queries where a good subsequence exists after each update.
"""
import math


class Solution:
    """Provides method to count queries with good subsequences."""

    def countGoodSubseq(self, nums, p, queries):
        """
        Return the number of queries after which there exists a good subsequence.

        A good subsequence is a non-empty subsequence whose length is strictly
        less than n and whose greatest common divisor (GCD) is exactly p.
        """
        n = len(nums)
        if n <= 6:
            return self._count_small(nums, p, queries)
        return self._count_large(nums, p, queries)

    def _count_small(self, nums, p, queries):
        """
        Brute force approach for n <= 6.

        Since n is small, we can test every strict non-empty subset.
        The total number of such subsets is at most 2^6 - 2 = 62.
        """
        n = len(nums)
        masks = [mask for mask in range(1, (1 << n) - 1)]
        ans = 0

        for ind, val in queries:
            nums[ind] = val
            for mask in masks:
                gcd_val = 0
                for i in range(n):
                    if mask & (1 << i):
                        gcd_val = math.gcd(gcd_val, nums[i])
                if gcd_val == p:
                    ans += 1
                    break
        return ans

    def _count_large(self, nums, p, queries):
        """
        Efficient approach for n > 6.

        Uses a segment tree to maintain the GCD of all elements that are
        multiples of p. Additionally counts how many elements are exactly
        p and how many are multiples of p.

        The logic:
        - If there is an element equal to p, the singleton [p] is good.
        - If no element is a multiple of p, no subsequence can have GCD p.
        - Otherwise, consider the GCD of all multiples of p.
          * If not all elements are multiples (count_mul < n), we can take
            the whole set of multiples; if its GCD is p, it is a good subset.
          * If all elements are multiples (count_mul == n) and the GCD of
            all elements is p, then for n > 6 it is always possible to find
            a strict subset with GCD p (based on number‑theoretic properties).
        """
        n = len(nums)

        # Build segment tree storing nums[i] if nums[i] % p == 0 else 0.
        size = 1
        while size < n:
            size <<= 1
        seg_tree = [0] * (2 * size)

        for i, value in enumerate(nums):
            if value % p == 0:
                seg_tree[size + i] = value
        for i in range(size - 1, 0, -1):
            seg_tree[i] = math.gcd(seg_tree[2 * i], seg_tree[2 * i + 1])

        # Initial counters.
        count_eq_p = sum(1 for x in nums if x == p)
        count_mul_p = sum(1 for x in nums if x % p == 0)

        ans = 0

        for ind, val in queries:
            old = nums[ind]

            # Update counters.
            if old == p:
                count_eq_p -= 1
            if old % p == 0:
                count_mul_p -= 1
            if val == p:
                count_eq_p += 1
            if val % p == 0:
                count_mul_p += 1
            nums[ind] = val

            # Update segment tree at position ind.
            pos = size + ind
            seg_tree[pos] = val if val % p == 0 else 0
            pos //= 2
            while pos >= 1:
                seg_tree[pos] = math.gcd(seg_tree[2 * pos], seg_tree[2 * pos + 1])
                pos //= 2

            # Decide if a good subsequence exists after this query.
            if count_eq_p > 0:
                # A single element equal to p already forms a good subsequence.
                ans += 1
            elif count_mul_p == 0:
                # No element is a multiple of p -> impossible.
                continue
            else:
                gcd_all_multiples = seg_tree[1]
                if count_mul_p < n:
                    # We can take the whole set of multiples (strict subset).
                    if gcd_all_multiples == p:
                        ans += 1
                else:  # count_mul_p == n
                    # All elements are multiples of p.
                    # For n > 6, if the GCD of all elements is p,
                    # a strict subset with GCD p is guaranteed to exist.
                    if gcd_all_multiples == p:
                        ans += 1

        return ans
