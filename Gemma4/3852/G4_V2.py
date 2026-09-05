"""
Dieses Modul enthält die Lösung zur Findung des kleinsten Paares
von Zahlen mit unterschiedlichen Häufigkeiten in einer Liste.
"""
from collections import Counter


class Solution:
    """
    Klasse zur Lösung des Problems der minimalen distinkten Frequenzpaare.
    """

    def min_distinct_freq_pair(self, nums):
        """
        Findet das Paar [x, y] mit x < y und unterschiedlichen Frequenzen,
        wobei x und dann y minimiert werden.

        :type nums: List[int]
        :rtype: List[int]
        """
        # 1. Frequenzen aller Zahlen zählen
        counts = Counter(nums)

        # 2. Die eindeutigen Zahlen sortiert extrahieren
        unique_elements = sorted(counts.keys())

        # 3. Alle Paare (x, y) prüfen wobei x < y
        # Die Verwendung von enumerate erfüllt die Pylint-Anforderung C0200
        for i, x in enumerate(unique_elements):
            # Wir prüfen alle Elemente, die nach dem aktuellen Index i kommen
            for y in unique_elements[i + 1:]:
                # Bedingung: Die Frequenzen müssen unterschiedlich sein
                if counts[x] != counts[y]:
                    return [x, y]

        # 4. Wenn keine gültigen Paare gefunden wurden
        return [-1, -1]
