"""
This module provides a solution to find the minimum XOR path cost in a 2D grid.
The goal is to move from the top-left to the bottom-right cell using only
right and down moves, minimizing the XOR sum of all visited cells.
"""

class Solution:
    """
    A class containing the method to calculate the minimum XOR cost
    to travel from the top-left to the bottom-right of a grid.
    """

    def minCost(self, grid):
        """
        Calculates the minimum possible XOR value among all valid paths.

        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        # dp[i][j] stores all possible XOR values reachable at cell (i, j).
        # Given grid values are <= 1023, the XOR sum will not exceed 1023.
        dp = [[set() for _ in range(n)] for _ in range(m)]

        # Initialize the starting cell
        dp[0][0].add(grid[0][0])

        # Fill the first row (can only come from the left)
        for j in range(1, n):
            val = grid[0][j]
            for prev_xor in dp[0][j-1]:
                dp[0][j].add(prev_xor ^ val)

        # Fill the first column (can only come from above)
        for i in range(1, m):
            val = grid[i][0]
            for prev_xor in dp[i-1][0]:
                dp[i][0].add(prev_xor ^ val)

        # Fill the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                # Transition from the cell above
                for prev_xor in dp[i-1][j]:
                    dp[i][j].add(prev_xor ^ val)
                # Transition from the cell to the left
                for prev_xor in dp[i][j-1]:
                    dp[i][j].add(prev_xor ^ val)

        # Return the minimum value found in the destination cell's set
        return min(dp[m-1][n-1])
