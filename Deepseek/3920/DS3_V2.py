"""
Dieses Modul bietet eine Lösung zur Berechnung der maximalen Anzahl
an Fixed Points in einem Array nach beliebigen Löschungen.
"""
import bisect


class Solution(object):
    """
    Klasse zur Berechnung der maximalen Fixed Points.
    Ein Fixed Point ist definiert als ein Element, dessen Wert seinem Index entspricht.
    """

    def maxFixedPoints(self, nums):
        """
        Berechnet die maximale Anzahl an Fixed Points, die durch Löschen 
        von Elementen erreicht werden können.

        :type nums: List[int]
        :rtype: int
        """
        # Ein Element an Index i mit Wert v kann ein Fixed Point werden,
        # wenn v <= i. Die Anzahl der zu löschenden Elemente links davon ist d = i - v.
        # Damit mehrere Elemente Fixed Points werden, muss die Anzahl der
        # Löschungen (d) nicht-abnehmend sein und die Werte (v) strikt steigend.
        
        candidates = []
        for i, v in enumerate(nums):
            if i >= v:
                # Wir speichern die Differenz d und den Wert v.
                candidates.append((i - v, v))

        if not candidates:
            return 0

        # Um die LIS (Longest Increasing Subsequence) in 2D zu finden:
        # 1. Sortiere primär nach der Differenz d (aufsteigend).
        # 2. Sortiere sekundär nach dem Wert v (aufsteigend).
        # Da d nicht-abnehmend sein darf, erlaubt die Sortierung uns, 
        # nur noch eine LIS auf den Werten v zu berechnen.
        candidates.sort()

        # LIS auf den Werten v mit O(N log N) Zeitkomplexität
        tails = []
        for _, v in candidates:
            # Wir suchen die Position, an der v in die tails-Liste passt.
            # Da v strikt steigen muss, nutzen wir bisect_left.
            idx = bisect.bisect_left(tails, v)
            if idx < len(tails):
                tails[idx] = v
            else:
                tails.append(v)

        return len(tails)


# Pylint-Anмечаungen: 
# Die Methodennamen folgen der Vorgabe des Users (CamelCase), 
# nicht dem PEP8 (snake_case). 
# Die Vererbung von 'object' ist in Python 3 redundant, wurde aber beibehalten,
# da sie Teil der geforderten Syntax ist.
