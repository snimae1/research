import math

class Solution(object):
    def countGoodSubseq(self, nums, p, queries):
        """
        :type nums: List[int]
        :type p: int
        :type queries: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        
        # For very small n we can just brute force all proper subsequences.
        if n <= 6:
            # Precompute bit masks for all non-empty, strict subsets
            masks = []
            for mask in range(1, (1 << n) - 1):
                masks.append(mask)
            
            for ind, val in queries:
                nums[ind] = val
                good = False
                for mask in masks:
                    g = 0
                    for i in range(n):
                        if mask & (1 << i):
                            g = math.gcd(g, nums[i])
                    if g == p:
                        good = True
                        break
                if good:
                    ans += 1
            return ans
        
        # ---------- n > 6 ----------
        # Build a segment tree that stores for each index:
        # nums[i] if nums[i] % p == 0  else  0
        # gcd(0, x) = x, so the tree root gives gcd of all multiples of p.
        size = 1
        while size < n:
            size <<= 1
        tree = [0] * (2 * size)
        
        for i in range(n):
            if nums[i] % p == 0:
                tree[size + i] = nums[i]
        for i in range(size - 1, 0, -1):
            tree[i] = math.gcd(tree[2 * i], tree[2 * i + 1])
        
        # Counters
        count_eq = 0   # number of elements exactly equal to p
        count_mul = 0  # number of elements that are multiples of p
        for x in nums:
            if x == p:
                count_eq += 1
            if x % p == 0:
                count_mul += 1
        
        for ind, val in queries:
            old = nums[ind]
            
            # Update counters
            if old == p:
                count_eq -= 1
            if old % p == 0:
                count_mul -= 1
            if val == p:
                count_eq += 1
            if val % p == 0:
                count_mul += 1
            nums[ind] = val
            
            # Update segment tree
            pos = size + ind
            tree[pos] = val if val % p == 0 else 0
            pos //= 2
            while pos >= 1:
                tree[pos] = math.gcd(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2
            
            # Decide after the query
            if count_eq > 0:
                # A single element equal to p already forms a good subsequence
                ans += 1
            elif count_mul == 0:
                # No multiple of p exists -> impossible to get gcd exactly p
                continue
            else:
                G = tree[1]   # gcd of all multiples of p
                if count_mul < n:
                    # We can take the whole set of multiples (size < n)
                    if G == p:
                        ans += 1
                else:  # count_mul == n
                    # All elements are multiples of p. Need a strict subset.
                    # gcd of whole array is G. If G != p -> impossible.
                    # If G == p: since n > 6, a strict subset with gcd p
                    # always exists (a minimal counterexample needs n <= 6).
                    if G == p:
                        ans += 1
        
        return ans
