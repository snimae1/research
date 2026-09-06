"""
Dieses Modul bietet eine Lösung zur Berechnung der maximalen Subarray-Summe,
wenn eine begrenzte Anzahl von Elementtauschen (k) erlaubt ist.
"""


class Solution:
    """
    Klasse zur Lösung des Maximum Subarray Sum Problems mit k erlaubten Swaps.
    """

    def calculate_swapped_sum(self, current_sum, window_elements, indexed_sorted, i, j, k):
        """
        Berechnet die optimierte Summe für ein Fenster durch den Tausch von
        kleinen Elementen im Fenster gegen große Elemente außerhalb.
        """
        n = len(indexed_sorted)
        window_len = len(window_elements)
        # Max. Swaps: Limit k, verfügbare Elemente im Fenster, verfügbare extern
        max_swaps = min(k, window_len, n - window_len)

        if max_swaps == 0:
            return current_sum

        # Elemente im Fenster aufsteigend sortieren, um die kleinsten zuerst zu ersetzen
        win_sorted = sorted(window_elements)
        temp_sum = current_sum
        swaps_made = 0

        for val, idx in indexed_sorted:
            if idx < i or idx > j:
                smallest_inside = win_sorted[swaps_made]
                if val > smallest_inside:
                    temp_sum += (val - smallest_inside)
                    swaps_made += 1
                    if swaps_made == max_swaps:
                        break
                else:
                    # Da indexed_sorted absteigend ist, finden wir keine besseren Werte mehr
                    break
        return temp_sum

    def max_sum(self, nums, k):
        """
        Findet die maximal mögliche Subarray-Summe nach maximal k Swaps.
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        # Liste aller Elemente sortiert nach Wert (absteigend) mit Original-Index
        indexed_sorted = sorted(
            [(nums[x], x) for x in range(n)], key=lambda x: x[0], reverse=True
        )

        max_total_sum = float('-inf')

        for i in range(n):
            current_win_sum = 0
            for j in range(i, n):
                current_win_sum += nums[j]
                window_elements = nums[i:j+1]

                # Berechnung der bestmöglichen Summe für dieses spezifische Fenster
                result_sum = self.calculate_swapped_sum(
                    current_win_sum, window_elements, indexed_sorted, i, j, k
                )
                max_total_sum = max(max_total_sum, result_sum)

        return max_total_sum
