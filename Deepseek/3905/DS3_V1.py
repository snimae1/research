from typing import List
from collections import deque

class Solution(object):
    def colorGrid(self, n, m, sources):
        """
        :type n: int
        :type m: int
        :type sources: List[List[int]]
        :rtype: List[List[int]]
        """
        # Initialize grid and distance array
        grid = [[0] * m for _ in range(n)]
        dist = [[-1] * m for _ in range(n)]
        q = deque()
        
        # Set initial sources
        for r, c, color in sources:
            grid[r][c] = color
            dist[r][c] = 0
            q.append((r, c))
        
        # Directions: up, down, left, right
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while q:
            # Current distance of all nodes in the queue
            curr_dist = dist[q[0][0]][q[0][1]]
            proposals = {}
            
            # Process the entire current level
            for _ in range(len(q)):
                r, c = q.popleft()
                cur_color = grid[r][c]
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] == -1:
                        # Neighbor not yet colored: store the maximum color reaching it
                        if (nr, nc) in proposals:
                            if cur_color > proposals[(nr, nc)]:
                                proposals[(nr, nc)] = cur_color
                        else:
                            proposals[(nr, nc)] = cur_color
            
            # Assign colors to all newly reached cells and add them to the queue
            for (nr, nc), color in proposals.items():
                dist[nr][nc] = curr_dist + 1
                grid[nr][nc] = color
                q.append((nr, nc))
        
        return grid
