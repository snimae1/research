"""Lösung für die Aufgabe 'Maximum Alternating Subsequence Sum'."""

from bisect import bisect_left


class FenwickTree:
    """Fenwick-Baum für Maximum-Abfragen und Updates."""

    def __init__(self, size):
        """Erstellt einen Fenwick-Baum der angegebenen Größe."""
        self.tree = [float("-inf")] * (size + 1)
        self.size = size

    def update(self, index, value):
        """Speichert den maximalen Wert an der Position index."""
        while index <= self.size:
            self.tree[index] = max(self.tree[index], value)
            index += index & -index

    def query(self, index):
        """Gibt das Maximum im Bereich [1, index] zurück."""
        result = float("-inf")

        while index > 0:
            result = max(result, self.tree[index])
            index -= index & -index

        return result


class Solution:
    """Berechnet die maximale Summe einer gültigen alternierenden Teilfolge."""

    # pylint: disable=invalid-name
    def maxAlternatingSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        values = sorted(set(nums))
        size = len(values)

        # down_tree speichert Folgen, die mit 'größer als' enden.
        # up_tree speichert Folgen, die mit 'kleiner als' enden.
        down_tree = FenwickTree(size)
        up_tree = FenwickTree(size)

        down = [0] * len(nums)
        up = [0] * len(nums)
        answer = 0

        for i, value in enumerate(nums):
            # Nur Positionen mit mindestens k Abstand dürfen Vorgänger sein.
            j = i - k

            if j >= 0:
                previous = bisect_left(values, nums[j]) + 1
                reversed_previous = size - previous + 1

                down_tree.update(previous, down[j])
                up_tree.update(reversed_previous, up[j])

            rank = bisect_left(values, value) + 1

            # Die aktuelle Zahl kann immer eine neue Folge der Länge 1 bilden.
            up[i] = value
            down[i] = value

            # Vorgänger < value:
            # Die vorherige Folge muss mit einem '>' geendet haben.
            best = down_tree.query(rank - 1)
            if best != float("-inf"):
                up[i] = best + value

            # Vorgänger > value:
            # Die vorherige Folge muss mit einem '<' geendet haben.
            best = up_tree.query(size - rank)
            if best != float("-inf"):
                down[i] = best + value

            answer = max(answer, up[i], down[i])

        return answer
