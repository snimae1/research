class Solution(object):
    def maxTotalValue(self, value, decay, m):
        """
        :type value: List[int]
        :type decay: List[int]
        :type m: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(value)
        
        # Total number of strictly positive selections and their sum
        total_pos = 0
        total_pos_sum = 0
        for v, d in zip(value, decay):
            # number of times we can select i before the gain drops to <= 0
            t = (v + d - 1) // d
            total_pos += t
            # sum of the first t gains: t*v - d * t*(t-1)//2
            total_pos_sum += t * v - d * t * (t - 1) // 2
            
        # If we are allowed to take all positive gains (or more), just take them all
        if m >= total_pos:
            return total_pos_sum % MOD
        
        # Binary search for the threshold marginal gain X such that
        # count of gains >= X is >= m and count of gains >= X+1 is < m.
        low, high = 1, max(value)
        ans_X = 1
        while low <= high:
            mid = (low + high) // 2
            cnt = 0
            for v, d in zip(value, decay):
                if v >= mid:
                    cnt += (v - mid) // d + 1
                    if cnt >= m:   # early exit
                        break
            if cnt >= m:
                ans_X = mid
                low = mid + 1
            else:
                high = mid - 1
                
        X = ans_X
        threshold = X + 1
        
        # Sum all gains strictly greater than X
        sum_gt = 0
        cnt_gt = 0
        for v, d in zip(value, decay):
            if v >= threshold:
                t = (v - threshold) // d + 1
                cnt_gt += t
                sum_gt += t * v - d * t * (t - 1) // 2
                
        # Fill the remaining allowed selections with gains equal to X
        remaining = m - cnt_gt
        total = sum_gt + remaining * X
        
        return total % MOD
