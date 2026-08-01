class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        MAX_XOR = 1024  # grid values ≤ 1023, so XOR results are in [0, 1023]
        
        # dp_curr[j][k] is True if XOR value k can be achieved at cell (current_row, j)
        dp_curr = [[False] * MAX_XOR for _ in range(n)]
        dp_curr[0][grid[0][0]] = True
        
        # first row (can only come from left)
        for j in range(1, n):
            val = grid[0][j]
            for k in range(MAX_XOR):
                if dp_curr[j - 1][k]:
                    dp_curr[j][k ^ val] = True
        
        # remaining rows
        for i in range(1, m):
            dp_next = [[False] * MAX_XOR for _ in range(n)]
            
            # first column (can only come from top)
            val = grid[i][0]
            for k in range(MAX_XOR):
                if dp_curr[0][k]:
                    dp_next[0][k ^ val] = True
            
            # rest of the columns (from top or left)
            for j in range(1, n):
                val = grid[i][j]
                for k in range(MAX_XOR):
                    if dp_curr[j][k] or dp_next[j - 1][k]:
                        dp_next[j][k ^ val] = True
            
            dp_curr = dp_next
        
        # the answer is the smallest k with dp_curr[-1][k] == True
        for k in range(MAX_XOR):
            if dp_curr[-1][k]:
                return k
        return -1  # should never be reached
