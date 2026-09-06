"""
This module provides a solution to color a grid based on multiple sources
using a Multi-Source Breadth-First Search (BFS) algorithm.
"""
from collections import deque

# pylint: disable=too-few-public-methods
class Solution:
    """
    Contains the logic to spread colors across a grid from multiple sources.
    """

    # pylint: disable=invalid-name
    def colorGrid(self, n, m, sources):
        """
        Colors the grid based on the provided sources and rules.

        :type n: int
        :type m: int
        :type sources: List[List[int]]
        :rtype: List[List[int]]
        """
        # Initialize the grid with 0 (uncolored)
        grid = [[0] * m for _ in range(n)]

        # Sort sources descending by color value.
        # This ensures that if multiple colors reach a cell at the same time,
        # the one with the maximum value is processed first.
        sources.sort(key=lambda x: x[2], reverse=True)

        queue = deque()

        # Set initial colors in the grid and add them to the queue
        for r, c, color in sources:
            grid[r][c] = color
            queue.append((r, c))

        # Directions for spreading (up, down, left, right)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # BFS Process
        while queue:
            r, c = queue.popleft()
            current_color = grid[r][c]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check if the neighbor cell is within bounds and uncolored
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                    grid[nr][nc] = current_color
                    queue.append((nr, nc))

        return grid
