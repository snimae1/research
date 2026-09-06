"""
Dieses Modul stellt eine Lösung zur Berechnung des ersten stabilen Index
eines Arrays basierend auf einem Instabilitätsscore bereit.
"""

class Solution:
    """
    Klasse zur Lösung des Problems der Instabilitätsbewertung.
    """

    def first_stable_index(self, nums, k):
        """
        Findet den kleinsten Index i, an dem die Differenz zwischen dem 
        Maximum des Präfixes [0...i] und dem Minimum des Suffixes [i...n-1]
        kleiner oder gleich k ist.

        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1

        # Schritt 1: Berechne das Minimum für jeden Suffix [i...n-1]
        # suffix_min[i] speichert den kleinsten Wert von Index i bis zum Ende.
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        # Schritt 2: Iteriere durch die Liste und tracke das laufende Maximum (Präfix)
        current_max = float('-inf')
        for i in range(n):
            # Update des Maximums von nums[0...i]
            if nums[i] > current_max:
                current_max = nums[i]

            # Instability Score = max(nums[0..i]) - min(nums[i..n-1])
            instability_score = current_max - suffix_min[i]

            # Prüfen, ob der Index stabil ist
            if instability_score <= k:
                return i

        return -1

# pylint: disable=too-few-public-methods
