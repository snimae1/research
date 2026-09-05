"""
Dieses Modul enthält die Lösung für das GCD-Summen-Problem.
Es berechnet die Summe der GCDs von Paaren, die aus einem
modifizierten Prefix-GCD-Array gebildet werden.
"""
import math


class Solution:
    """
    Klasse zur Lösung der GCD-Summen-Aufgabe.
    """

    def gcd_sum(self, nums):
        """
        Berechnet die Summe der GCDs der gebildeten Paare.

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix_gcd = []
        mxi = 0

        # Schritt 1: Konstruktion von prefix_gcd
        for num in nums:
            # Aktualisiere das bisherige Maximum (mxi)
            if num > mxi:
                mxi = num

            # Berechne den GCD von aktuellem Element und dem Maximum
            prefix_gcd.append(math.gcd(num, mxi))

        # Schritt 2: Sortiere prefix_gcd in nicht-absteigender Reihenfolge
        prefix_gcd.sort()

        # Schritt 3 & 4: Pairing und Berechnung der Summe
        return self._calculate_pair_gcd_sum(prefix_gcd)

    def _calculate_pair_gcd_sum(self, sorted_gcds):
        """
        Hilfsmethode, um Paare aus dem sortierten Array zu bilden
        und die Summe ihrer GCDs zu berechnen.
        """
        total_gcd_sum = 0
        left = 0
        right = len(sorted_gcds) - 1

        # Wir laufen von beiden Seiten zur Mitte.
        # Das mittlere Element bei ungeraden n bleibt automatisch übrig.
        while left < right:
            total_gcd_sum += math.gcd(sorted_gcds[left], sorted_gcds[right])
            left += 1
            right -= 1

        return total_gcd_sum
