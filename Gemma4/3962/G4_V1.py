class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        # Erstelle eine Liste aller Elemente sortiert nach Wert (absteigend),
        # inklusive ihres Original-Index, um zu prüfen, ob sie im aktuellen Fenster liegen.
        indexed_sorted = sorted([(nums[x], x) for x in range(n)], key=lambda x: x[0], reverse=True)
        
        max_total_sum = float('-inf')

        # Iteriere über alle möglichen Startpunkte i des Subarrays
        for i in range(n):
            current_win_sum = 0
            # Iteriere über alle möglichen Endpunkte j des Subarrays
            for j in range(i, n):
                current_win_sum += nums[j]
                
                # Die Länge des aktuellen Fensters
                window_len = j - i + 1
                
                # Wir können maximal so viele Swaps machen wie:
                # 1. Das Limit k erlaubt.
                # 2. Elemente im Fenster vorhanden sind (können nicht mehr als window_len ersetzen).
                # 3. Elemente außerhalb des Fensters verfügbar sind.
                max_swaps_possible = min(k, window_len, n - window_len)
                
                if max_swaps_possible == 0:
                    max_total_sum = max(max_total_sum, current_win_sum)
                    continue

                # Sortiere die Elemente im aktuellen Fenster aufsteigend, 
                # damit wir die kleinsten Werte zuerst ersetzen können.
                win_sorted = sorted(nums[i:j+1])
                
                temp_sum = current_win_sum
                swaps_made = 0
                
                # Suche in der global sortierten Liste nach den größten Elementen,
                # die sich NICHT im Indexbereich [i, j] befinden.
                for val, idx in indexed_sorted:
                    if idx < i or idx > j:
                        # Prüfe, ob das externe Element größer ist als das kleinste im Fenster
                        smallest_inside = win_sorted[swaps_made]
                        if val > smallest_inside:
                            temp_sum += (val - smallest_inside)
                            swaps_made += 1
                            # Stop, wenn k Swaps erreicht sind oder keine weiteren Tausche möglich sind
                            if swaps_made == max_swaps_possible:
                                break
                        else:
                            # Da indexed_sorted absteigend ist, wird kein weiteres externes Element 
                            # mehr größer als die verbleibenden Elemente im win_sorted sein.
                            break
                
                max_total_sum = max(max_total_sum, temp_sum)

        return max_total_sum
