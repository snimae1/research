from collections import deque

class Solution(object):

    def colorGrid(self, n, m, sources):
        """
        :type n: int
        :type m: int
        :type sources: List[List[int]]
        :rtype: List[List[int]]
        """
        # Initialisiere das Gitter mit 0 (unfarbig)
        grid = [[0] * m for _ in range(n)]
        
        # Sortiere die Quellen absteigend nach der Farbe (Index 2).
        # Dies stellt sicher, dass bei gleichem Zeitschritt die Farbe mit dem
        # maximalen Wert zuerst in die Queue kommt und die Zelle besetzt.
        sources.sort(key=lambda x: x[2], reverse=True)
        
        queue = deque()
        
        # Setze Startfarben im Gitter und füge sie der Queue hinzu
        for r, c, color in sources:
            grid[r][c] = color
            queue.append((r, c))
            
        # Richtungen für die Ausbreitung (oben, unten, links, rechts)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # BFS Prozess
        while queue:
            r, c = queue.popleft()
            current_color = grid[r][c]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Prüfen, ob die Nachbarzelle innerhalb der Grenzen liegt 
                # und noch nicht gefärbt wurde (grid[nr][nc] == 0)
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                    grid[nr][nc] = current_color
                    queue.append((nr, nc))
                    
        return grid
