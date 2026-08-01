class Solution(object):
    def maxFixedPoints(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # groups[A] will store all d = i - A for valid elements with value A
        groups = [[] for _ in range(n)]
        for i, val in enumerate(nums):
            if val <= i:
                groups[val].append(i - val)
        
        # Fenwick tree (BIT) for prefix maximum
        bit_size = n + 2
        bit = [0] * bit_size
        
        def bit_update(i, val):
            while i < bit_size:
                if val > bit[i]:
                    bit[i] = val
                i += i & -i
                
        def bit_query(i):
            res = 0
            while i > 0:
                if bit[i] > res:
                    res = bit[i]
                i -= i & -i
            return res
        
        ans = 0
        # Process groups in increasing order of A (strictly increasing A is required)
        for A in range(n):
            if not groups[A]:
                continue
            temp = []
            # Compute dp values using BIT state from smaller A only
            for d in groups[A]:
                # d is in [0, n-1], BIT is 1-indexed
                best = bit_query(d + 1)
                temp.append((d, best + 1))
            # Update BIT with the new values of the current A group
            for d, val in temp:
                bit_update(d + 1, val)
                if val > ans:
                    ans = val
                    
        return ans
