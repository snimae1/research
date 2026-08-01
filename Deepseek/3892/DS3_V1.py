class Solution(object):
    def minOperations(self, nums, k):
        n = len(nums)
        if k == 0:
            return 0
        if k > n // 2:
            return -1
        
        # cost to make each index a peak independently
        c = [0] * n
        for i in range(n):
            left = nums[i - 1] if i > 0 else nums[-1]
            right = nums[i + 1] if i < n - 1 else nums[0]
            req = max(left, right) + 1
            if req > nums[i]:
                c[i] = req - nums[i]
            else:
                c[i] = 0
        
        INF = 10**15
        
        def solve_linear(costs, need):
            """Min cost to select exactly `need` non-adjacent elements from a linear array."""
            m = len(costs)
            if need == 0:
                return [0]
            max_possible = (m + 1) // 2
            need = min(need, max_possible)
            
            # dp0[j] = min cost for j selections, last element NOT taken
            # dp1[j] = min cost for j selections, last element taken
            dp0 = [INF] * (need + 1)
            dp1 = [INF] * (need + 1)
            dp0[0] = 0
            if need >= 1:
                dp1[1] = costs[0]
                
            for i in range(1, m):
                cst = costs[i]
                limit = min(need, (i + 2) // 2)
                new_dp0 = [INF] * (need + 1)
                new_dp1 = [INF] * (need + 1)
                for j in range(limit + 1):
                    # skip current element
                    v0 = dp0[j]
                    v1 = dp1[j]
                    new_dp0[j] = v0 if v0 < v1 else v1
                    # take current element
                    if j > 0:
                        prev = dp0[j - 1]
                        if prev < INF:
                            new_dp1[j] = prev + cst
                dp0, dp1 = new_dp0, new_dp1
                
            return [min(dp0[j], dp1[j]) for j in range(need + 1)]
        
        # Case 1: do not make index 0 a peak
        res1 = solve_linear(c[1:], k)
        ans1 = res1[k] if k < len(res1) else INF
        
        # Case 2: make index 0 a peak
        if k == 1:
            ans2 = c[0]
        else:
            # need k-1 peaks from indices 2 to n-2
            sub2 = c[2:n-1]
            if not sub2:
                ans2 = INF
            else:
                res2 = solve_linear(sub2, k - 1)
                if k - 1 < len(res2):
                    ans2 = c[0] + res2[k - 1]
                else:
                    ans2 = INF
        
        ans = min(ans1, ans2)
        return ans if ans < INF else -1
