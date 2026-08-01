class Solution(object):

    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """ 
        n = len(nums)
        
        # Spezialfall: Wenn keine Gipfel benötigt werden, sind 0 Operationen nötig.
        if k == 0:
            return 0
        
        # In einem kreisförmigen Array können maximal n // 2 Gipfel existieren,
        # da zwei Gipfel niemals direkt nebeneinander liegen dürfen.
        if k > n // 2:
            return -1

        # Schritt 1: Berechne die Kosten, um jedes Element an Index i zu einem Peak zu machen.
        costs = [0] * n
        for i in range(n):
            prev_val = nums[i - 1] # Python-Index -1 greift automatisch auf das letzte Element zu
            next_val = nums[(i + 1) % n]
            # Die Kosten sind die Differenz zum benötigten Wert (max der Nachbarn + 1)
            costs[i] = max(0, max(prev_val, next_val) + 1 - nums[i])

        def get_min_cost_linear(current_costs, target):
            """
            Hilfsfunktion: Berechnet die minimalen Kosten für 'target' Gipfel 
            in einem linearen Array (keine Überlappung/Zirkularität innerhalb der Liste).
            """
            if target == 0:
                return 0
            m = len(current_costs)
            # Unmöglich, mehr Gipfel zu platzieren als mathematisch möglich ist
            if m < (2 * target - 1):
                return float('inf')

            # dp[j] speichert die minimalen Kosten für j Gipfel.
            # Wir benötigen den Zustand von i-1 und i-2, um die Nicht-Benachbarung sicherzustellen.
            dp_prev_prev = [float('inf')] * (target + 1)
            dp_prev = [float('inf')] * (target + 1)
            dp_prev_prev[0] = 0
            dp_prev[0] = 0

            for i in range(m):
                curr_cost = current_costs[i]
                dp_curr = dp_prev[:] # Option: Element i wird ignoriert (kein Gipfel)
                for j in range(1, target + 1):
                    # Option: Element i wird als Gipfel gewählt. 
                    # Dann müssen wir zum Zustand von vor zwei Elementen zurückgreifen.
                    val = curr_cost + dp_prev_prev[j - 1]
                    if val < dp_curr[j]:
                        dp_curr[j] = val
                dp_prev_prev = dp_prev
                dp_prev = dp_curr
            
            return dp_prev[target]

        # Fall 1: Index 0 ist KEIN Gipfel.
        # Wir wählen k Gipfel aus den Indizes [1, ..., n-1].
        ans1 = get_min_cost_linear(costs[1:], k)

        # Fall 2: Index 0 IST ein Gipfel.
        # Dann können weder Index 1 noch Index n-1 Gipfel sein.
        # Wir wählen die restlichen (k-1) Gipfel aus den Indizes [2, ..., n-2].
        if k == 1:
            ans2 = costs[0]
        else:
            # Bereich von Index 2 bis n-2 inklusiv
            res_inner = get_min_cost_linear(costs[2:n-1], k - 1)
            ans2 = costs[0] + res_inner

        final_result = min(ans1, ans2)
        return final_result if final_result != float('inf') else -1
