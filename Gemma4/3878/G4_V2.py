"""
Modul zur Berechnung von 'guten' Subarrays basierend auf Bitwise-OR Operationen.
Ein Subarray ist gut, wenn sein bitweiser OR-Wert in diesem Subarray enthalten ist.
"""

class Solution:
    """
    Bietet eine Lösung zur Zählung von Subarrays, deren bitweiser OR-Wert 
    ein Element des Subarrays selbst ist.
    """

    def countGoodSubarrays(self, nums):
        """
         Berechnet die Anzahl der guten Subarrays in einer gegebenen Liste.

        :type nums: List[int]
        :rtype: int
        """
        total_good = 0
        # Speichert Paare von (or_wert, start_index) für Subarrays, die am aktuellen Index enden.
        # Da OR-Werte monoton steigen, gibt es maximal log2(max(nums)) distinkte Werte.
        active_or_ranges = []
        last_pos = {}

        for i, val in enumerate(nums):
            last_pos[val] = i

            # Neue OR-Werte basierend auf dem aktuellen Wert berechnen
            next_ors = []
            for v, idx in active_or_ranges:
                new_v = v | val
                if not next_ors or new_v != next_ors[-1][0]:
                    next_ors.append((new_v, idx))

            # Das Subarray aus nur einem Element (selbst) hinzufügen
            if not next_ors or val != next_ors[-1][0]:
                next_ors.append((val, i))

            active_or_ranges = next_ors

            # Prüfen, welche dieser OR-Bereiche ein 'gutes' Subarray bilden
            for j, (v, start_idx) in enumerate(active_or_ranges):
                # Ende des Bereichs für diesen spezifischen OR-Wert bestimmen
                end_range = active_or_ranges[j + 1][1] - 1 if j + 1 < len(active_or_ranges) else i

                if v in last_pos:
                    # Ein Subarray ist gut, wenn der OR-Wert v innerhalb des Bereichs liegt.
                    # Die letzte Position von v muss also >= Startindex des Subarrays sein.
                    valid_end = min(end_range, last_pos[v])
                    if valid_end >= start_idx:
                        total_good += (valid_end - start_idx + 1)

        return total_good
