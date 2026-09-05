"""
Dieses Modul löst das Problem der minimalen Operationen, um in einem
kreisförmigen Array eine bestimmte Anzahl an Gipfeln (Peaks) zu erzeugen.
"""

class Solution:
    """
    Bietet eine Lösung zur Berechnung der minimalen Kosten, um k nicht-benachbarte
    Elemente in einem kreisförmigen Array zu Gipfeln zu machen.
    """

    # pylint: disable=too-few-public-methods
    def minOperations(self, nums, k):
        """
        Berechnet die minimalen Operationen für mindestens k Gipfel.

        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # pylint: disable=invalid-name
        n = len(nums)

        if k == 0:
            return 0

        # In einem kreisförmigen Array können maximal n // 2 Gipfel existieren,
        # da zwei Gipfel niemals direkt nebeneinander liegen dürfen.
        if k > n // 2:
            return -1

        # Berechnung der Kosten für jedes Element, um es zu einem Peak zu machen.
        # Ein Element i ist ein Peak, wenn nums[i] > max(nums[i-1], nums[i+1]).
        costs = [0] * n
        for i in range(n):
            prev_val = nums[i - 1]
            next_val = nums[(i + 1) % n]
            costs[i] = max(0, max(prev_val, next_val) + 1 - nums[i])

        # Fall 1: Index 0 ist KEIN Gipfel.
        # Wir suchen k Gipfel im Bereich [1, n-1].
        ans1 = self._get_min_cost_linear(costs[1:], k)

        # Fall 2: Index 0 IST ein Gipfel.
        # Dann können Index 1 und Index n-1 keine Gipfel sein.
        # Wir suchen die restlichen k-1 Gipfel im Bereich [2, n-2].
        if k == 1:
            ans2 = costs[0]
        else:
            res_inner = self._get_min_cost_linear(costs[2:n - 1], k - 1)
            ans2 = costs[0] + res_inner

        final_result = min(ans1, ans2)
        return final_result if final_result != float('inf') else -1

    def _get_min_cost_linear(self, current_costs, target):
        """
        Hilfsmethode zur Berechnung der minimalen Kosten für 'target' Gipfel
        in einem linearen Array mittels Dynamischer Programmierung.
        """
        if target == 0:
            return 0
        m = len(current_costs)
        if m < (2 * target - 1):
            return float('inf')

        # dp_prev_prev: Min. Kosten für j Gipfel bis Index i-2
        # dp_prev: Min. Kosten für j Gipfel bis Index i-1
        dp_prev_prev = [float('inf')] * (target + 1)
        dp_prev = [float('inf')] * (target + 1)
        dp_prev_prev[0] = 0
        dp_prev[0] = 0

        for i in range(m):
            curr_cost = current_costs[i]
            # Initialisiere aktuellen Zustand mit den Werten von i-1 (Element i wird ignoriert)
            dp_curr = dp_prev[:]
            for j in range(1, target + 1):
                # Element i wird als Gipfel gewählt:
                # Kosten = Kosten von i + Min. Kosten für j-1 Gipfel bis Index i-2
                val = curr_cost + dp_prev_prev[j - 1]
                if val < dp_curr[j]:
                    dp_curr[j] = val
            dp_prev_prev = dp_prev
            dp_prev = dp_curr

        return dp_prev[target]
