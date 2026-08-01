class Solution(object):
    def countArrays(self, digitSum):
        """
        :type digitSum: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        MAXV = 5000
        MAXSUM = 40

        # numbers grouped by digit sum
        groups = [[] for _ in range(MAXSUM + 1)]
        for x in range(MAXV + 1):
            s = 0
            y = x
            if y == 0:
                s = 0
            else:
                while y:
                    s += y % 10
                    y //= 10
            groups[s].append(x)

        # Impossible digit sum
        for s in digitSum:
            if s > MAXSUM or not groups[s]:
                return 0

        # DP for first position
        prev_vals = groups[digitSum[0]]
        prev_dp = [1] * len(prev_vals)

        # Process remaining positions
        for idx in range(1, len(digitSum)):
            cur_vals = groups[digitSum[idx]]

            # Prefix sums over previous DP
            prefix = [0] * (len(prev_dp) + 1)
            for i in range(len(prev_dp)):
                prefix[i + 1] = (prefix[i] + prev_dp[i]) % MOD

            cur_dp = [0] * len(cur_vals)

            p = 0
            for i, v in enumerate(cur_vals):
                while p < len(prev_vals) and prev_vals[p] <= v:
                    p += 1
                cur_dp[i] = prefix[p]

            prev_vals = cur_vals
            prev_dp = cur_dp

        return sum(prev_dp) % MOD
