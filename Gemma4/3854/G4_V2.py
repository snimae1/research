"""
Modul zur Lösung des Problems der paritätsalternierenden Arrays.
Ziel ist es, die minimale Anzahl an Operationen zu finden, um ein Array so zu 
verändern, dass sich gerade und ungerade Zahlen abwechseln, und dabei 
die Differenz zwischen Maximum und Minimum zu minimieren.
"""

import bisect


class Solution:
    """
    Bietet Methoden zur Berechnung der minimalen Kosten und des minimalen 
    Wertebereichs für paritätsalternierende Arrays.
    """

    def makeParityAlternating(self, nums):
        """
        Berechnet die minimale Anzahl an Operationen und den minimalen 
        möglichen Range (max - min) des resultierenden Arrays.

        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 1:
            return [0, 0]

        # Wir prüfen die zwei möglichen Muster: 
        # 1. Beginnt mit Gerade (0) 
        # 2. Beginnt mit Ungerade (1)
        res0_ops, res0_range = self._solve_for_pattern(nums, 0)
        res1_ops, res1_range = self._solve_for_pattern(nums, 1)

        # Wähle das Muster mit den geringsten Operationen
        if res0_ops < res1_ops:
            return [res0_ops, res0_range]
        if res1_ops < res0_ops:
            return [res1_ops, res1_range]
        
        # Bei Gleichstand der Operationen den minimalen Range wählen
        return [res0_ops, min(res0_range, res1_range)]

    def _solve_for_pattern(self, nums, start_parity):
        """
        Hilfsmethode, die die Kosten und den Range für ein spezifisches 
        Paritätsmuster berechnet.
        """
        fixed, changed, ops = self._get_parity_groups(nums, start_parity)
        
        # Wenn keine Elemente geändert werden müssen, ist der Range fix
        if not changed:
            current_range = max(fixed) - min(fixed) if fixed else 0
            return ops, current_range
            
        return ops, self._calculate_min_range(fixed, changed)

    def _get_parity_groups(self, nums, start_parity):
        """
        Teilt die Zahlen in 'fest' (Parität passt) und 'zu ändern' (Parität passt nicht) auf.
        """
        fixed = []
        changed = []
        ops = 0
        for i, val in enumerate(nums):
            target_parity = (start_parity + i) % 2
            if val % 2 == target_parity:
                fixed.append(val)
            else:
                ops += 1
                # Bei einer Änderung gibt es zwei Optionen: val-1 oder val+1
                changed.append((val - 1, val + 1))
        return fixed, changed, ops

    def _calculate_min_range(self, fixed, changed):
        """
        Minimiert max(nums) - min(nums) unter der Bedingung, dass 
        für jedes 'changed' Element entweder low oder high gewählt wird.
        """
        changed.sort()
        m = len(changed)
        
        # Prefix- und Suffix-Maxima zur effizienten Berechnung des Gesamtmaximums
        pre_max_high = [-float('inf')] * (m + 1)
        for i in range(m):
            pre_max_high[i + 1] = max(pre_max_high[i], changed[i][1])
            
        suf_max_low = [-float('inf')] * (m + 1)
        for i in range(m - 1, -1, -1):
            suf_max_low[i] = max(suf_max_low[i + 1], changed[i][0])
        
        # Das globale Minimum 'min_val' kann nicht größer sein als:
        # 1. Das kleinste 'high'-Element eines zu ändernden Wertes
        # 2. Das kleinste Element der fixen Werte
        limit = min(c[1] for c in changed)
        if fixed:
            limit = min(limit, min(fixed))
            
        max_fixed = max(fixed) if fixed else -float('inf')
        min_range = float('inf')
        
        # Kandidaten für das optimale Minimum des Arrays
        lows = [c[0] for c in changed]
        candidates = lows + [limit]
        
        for min_val in candidates:
            if min_val > limit:
                continue
                
            # Bestimme, welche Elemente zwingend auf 'high' gesetzt werden müssen,
            # weil ihr 'low'-Wert kleiner als das gewählte Minimum ist.
            k = bisect.bisect_left(lows, min_val)
            
            # Das Maximum des Arrays ergibt sich aus:
            # - dem Maximum der fixen Werte
            # - dem Maximum der 'high'-Werte (für i < k)
            # - dem Maximum der 'low'-Werte (für i >= k)
            current_max = max(max_fixed, pre_max_high[k], suf_max_low[k])
            
            # Der tatsächliche Range ist die Differenz vom Maximum zum gewählten Minimum
            actual_range = max(min_val, current_max) - min_val
            if actual_range < min_range:
                min_range = actual_range
                
        return int(min_range)
