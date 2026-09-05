"""
Solution for the minimum XOR path problem on a 2D grid.
"""


# pylint: disable=too-few-public-methods
class Solution(object):
    """
    LeetCode-style solution class.
    """

    # Maximum possible XOR value (grid values are 0..1023)
    MAX_XOR = 1024

    # pylint: disable=invalid-name
    def minCost(self, grid):
        """
        Return the minimum possible XOR value among all valid paths
        from (0, 0) to (m - 1, n - 1).

        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        max_xor = self.MAX_XOR

        # dp_curr[j][k] is True if XOR value k can be achieved at cell (current_row, j)
        dp_curr = [[False] * max_xor for _ in range(n)]
        dp_curr[0][grid[0][0]] = True

        # First row (can only be reached from the left)
        for j in range(1, n):
            val = grid[0][j]
            for k in range(max_xor):
                if dp_curr[j - 1][k]:
                    dp_curr[j][k ^ val] = True

        # Remaining rows
        for i in range(1, m):
            dp_next = [[False] * max_xor for _ in range(n)]

            # First column (can only be reached from above)
            val = grid[i][0]
            for k in range(max_xor):
                if dp_curr[0][k]:
                    dp_next[0][k ^ val] = True

            # Rest of the columns (from above or from the left)
            for j in range(1, n):
                val = grid[i][j]
                for k in range(max_xor):
                    if dp_curr[j][k] or dp_next[j - 1][k]:
                        dp_next[j][k ^ val] = True

            dp_curr = dp_next

        # Find the smallest achievable XOR value at the bottom-right cell
        for k in range(max_xor):
            if dp_curr[-1][k]:
                return k
        return -1  # Should never be reached given the constraints
