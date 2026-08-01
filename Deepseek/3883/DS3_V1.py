class Solution(object):
    def countArrays(self, digitSum):
        """
        :type digitSum: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        MAX_VAL = 5000
        
        # Precompute all numbers in [0, 5000] grouped by their digit sum.
        # Maximum possible digit sum for numbers <= 5000 is 31 (e.g., 4999),
        # but the problem allows digitSum[i] up to 50.
        digit_to_vals = [[] for _ in range(51)]
        for v in range(MAX_VAL + 1):
            s = sum(int(d) for d in str(v))
            if s <= 50:
                digit_to_vals[s].append(v)
        
        # If any required digit sum has no valid numbers, answer is 0.
        for s in digitSum:
            if not digit_to_vals[s]:
                return 0
        
        n = len(digitSum)
        
        # dp[v] = number of valid non-decreasing arrays ending with value v.
        dp = [0] * (MAX_VAL + 1)
        for v in digit_to_vals[digitSum[0]]:
            dp[v] = 1
            
        # Process remaining positions.
        for i in range(1, n):
            target_sum = digitSum[i]
            candidates = digit_to_vals[target_sum]  # already sorted
            
            # Build prefix sums over dp for quick range queries.
            pref = [0] * (MAX_VAL + 1)
            acc = 0
            for v in range(MAX_VAL + 1):
                acc = (acc + dp[v]) % MOD
                pref[v] = acc
                
            new_dp = [0] * (MAX_VAL + 1)
            for v in candidates:
                # Any previous value u <= v is allowed.
                new_dp[v] = pref[v]
            dp = new_dp
            
        return sum(dp) % MOD

