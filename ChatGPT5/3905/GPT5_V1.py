class Solution(object):
    def colorGrid(self, n, m, sources):
        """
        :type n: int
        :type m: int
        :type sources: List[List[int]]
        :rtype: List[List[int]]
        """

        from collections import deque

        # Ergebnis-Grid
        grid = [[0] * m for _ in range(n)]

        # Queue für Multi-Source-BFS
        # Speichert: (row, col, color)
        queue = deque()

        # Alle Quellen initialisieren
        for r, c, color in sources:
            grid[r][c] = color
            queue.append((r, c, color))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            # Alle Zellen dieser Zeitschritt-Ebene sammeln
            size = len(queue)
            next_cells = {}

            for _ in range(size):
                r, c, color = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < n and 0 <= nc < m:
                        # Nur noch nicht final eingefärbte Zellen betrachten
                        if grid[nr][nc] == 0:
                            # Falls mehrere Farben gleichzeitig ankommen,
                            # gewinnt die größere Farbe
                            if (nr, nc) not in next_cells:
                                next_cells[(nr, nc)] = color
                            else:
                                next_cells[(nr, nc)] = max(
                                    next_cells[(nr, nc)], color
                                )

            # Ergebnisse dieses Zeitschritts übernehmen
            for (r, c), color in next_cells.items():
                grid[r][c] = color
                queue.append((r, c, color))

        return grid
