"""Löst die Aufgabe der simultanen Farbausbreitung in einem Gitter."""

from collections import deque


class Solution:
    """Berechnet die finale Farbverteilung eines Gitters."""

    def colorGrid(self, n, m, sources):  # pylint: disable=invalid-name
        """
        Färbt das Gitter mittels einer Multi-Source-BFS.

        :param n: Anzahl der Zeilen.
        :param m: Anzahl der Spalten.
        :param sources: Liste der Startzellen [Zeile, Spalte, Farbe].
        :return: Das vollständig eingefärbte Gitter.
        """

        grid = [[0] * m for _ in range(n)]
        queue = deque()

        # Alle Quellen starten gleichzeitig bei Zeitschritt 0.
        for row, column, color in sources:
            grid[row][column] = color
            queue.append((row, column, color))

        while queue:
            # Eine komplette BFS-Ebene entspricht einem Zeitschritt.
            for _ in range(len(queue)):
                self._spread_color(queue, grid, m, n)

        return grid

    @staticmethod
    def _spread_color(queue, grid, width, height):
        """Verteilt eine Farbe auf die Nachbarzellen."""

        row, column, color = queue.popleft()

        for next_row, next_column in (
            (row - 1, column),
            (row + 1, column),
            (row, column - 1),
            (row, column + 1),
        ):
            if not (0 <= next_row < height and 0 <= next_column < width):
                continue

            # Noch nicht erreichte Zellen werden zunächst vorgemerkt.
            if grid[next_row][next_column] == 0:
                grid[next_row][next_column] = color
                queue.append((next_row, next_column, color))
