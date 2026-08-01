class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        MAXX = 1024  # grid values are < 1024, so every XOR is also < 1024

        # dp[j] = reachable XOR values at current row, column j
        dp = [None] * n

        for i in range(m):
            new_dp = [None] * n
            for j in range(n):
                val = grid[i][j]
                cur = [False] * MAXX

                if i == 0 and j == 0:
                    cur[val] = True
                else:
                    if i > 0:
                        for x in range(MAXX):
                            if dp[j][x]:
                                cur[x ^ val] = True
                    if j > 0:
                        for x in range(MAXX):
                            if new_dp[j - 1][x]:
                                cur[x ^ val] = True

                new_dp[j] = cur
            dp = new_dp

        for x in range(MAXX):
            if dp[n - 1][x]:
                return x
