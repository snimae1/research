"""Löst die Aufgabe der simultanen Farbausbreitung."""

from collections import deque


class Solution:
    """Verteilt Farben gleichzeitig von mehreren Startpunkten."""

    def colorGrid(self, n, m, sources):  # pylint: disable=invalid-name
        """
        Berechnet die finale Färbung des Gitters.

        :param n: Anzahl der Zeilen.
        :param m: Anzahl der Spalten.
        :param sources: Startpunkte im Format [Zeile, Spalte, Farbe].
        :return: Final eingefärbtes Gitter.
        """

        grid = [[0] * m for _ in range(n)]
        queue = deque()

        for row, column, color in sources:
            grid[row][column] = color
            queue.append((row, column, color))

        while queue:
            current_level = len(queue)
            candidates = {}

            for _ in range(current_level):
                row, column, color = queue.popleft()
                self._find_candidates(
                    row, column, color, grid, candidates, n, m
                )

            self._apply_candidates(grid, candidates, queue)

        return grid

    @staticmethod
    def _find_candidates(row, column, color, grid, candidates, rows, columns):
        """Sammelt alle Zellen, die im aktuellen Schritt erreicht werden."""

        for next_row, next_column in (
            (row - 1, column),
            (row + 1, column),
            (row, column - 1),
            (row, column + 1),
        ):
            if 0 <= next_row < rows and 0 <= next_column < columns:
                if grid[next_row][next_column] == 0:
                    position = (next_row, next_column)
                    candidates[position] = max(
                        color, candidates.get(position, 0)
                    )

    @staticmethod
    def _apply_candidates(grid, candidates, queue):
        """Übernimmt die Gewinnerfarben eines Zeitschritts."""

        for (row, column), color in candidates.items():
            grid[row][column] = color
            queue.append((row, column, color))
