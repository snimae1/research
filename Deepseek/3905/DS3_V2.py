# pylint: disable=invalid-name
"""Solution for the grid coloring problem."""
from collections import deque


class Solution:
    """Contains method to compute final grid colors after simultaneous spreading."""
    # pylint: disable=too-few-public-methods

    def colorGrid(self, n, m, sources):
        """
        Return the final grid after all possible color spreading.

        :type n: int
        :type m: int
        :type sources: List[List[int]]
        :rtype: List[List[int]]
        """
        # Initialise grid and distance array
        grid = [[0] * m for _ in range(n)]
        dist = [[-1] * m for _ in range(n)]
        queue = deque()

        # Set initial sources
        for r, c, color in sources:
            grid[r][c] = color
            dist[r][c] = 0
            queue.append((r, c))

        # Process level by level (BFS)
        while queue:
            current_dist = dist[queue[0][0]][queue[0][1]]
            proposals = {}

            # Examine all cells at the current distance
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for nr, nc in self._get_uncolored_neighbors(r, c, dist, n, m):
                    # Keep the maximum color if several sources reach the same cell
                    if (nr, nc) not in proposals or grid[r][c] > proposals[(nr, nc)]:
                        proposals[(nr, nc)] = grid[r][c]

            # Apply the proposals and enqueue newly colored cells
            for (nr, nc), color in proposals.items():
                dist[nr][nc] = current_dist + 1
                grid[nr][nc] = color
                queue.append((nr, nc))

        return grid

    def _get_uncolored_neighbors(self, r, c, dist, n, m):
        """Yield coordinates of uncolored neighboring cells."""
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] == -1:
                yield nr, nc
