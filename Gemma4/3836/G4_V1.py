import functools

class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums1)
        m = len(nums2)

        # Wir nutzen lru_cache für die Memoization, um bereits berechnete 
        # Zustände (i, j, p) zu speichern und nicht erneut berechnen zu müssen.
        @functools.lru_cache(None)
        def solve(i, j, p):
            # Basisfall 1: Wir haben erfolgreich k Paare gebildet.
            if p == 0:
                return 0
            
            # Basisfall 2: Wir haben ein Ende einer Liste erreicht, bevor 
            # wir k Paare bilden konnten. Wir geben einen sehr kleinen Wert zurück,
            # um diesen Pfad als ungültig zu markieren.
            if i == n or j == m:
                return float('-inf')

            # Es gibt drei Möglichkeiten an jedem Schritt:
            
            # 1. Wir bilden ein Paar aus nums1[i] und nums2[j].
            # Dann erhöhen wir beide Indizes und verringern die Anzahl der benötigten Paare.
            res_pair = (nums1[i] * nums2[j]) + solve(i + 1, j + 1, p - 1)
            
            # 2. Wir überspringen das aktuelle Element in nums1.
            res_skip_i = solve(i + 1, j, p)
            
            # 3. Wir überspringen das aktuelle Element in nums2.
            res_skip_j = solve(i, j + 1, p)
            
            # Wir nehmen das Maximum der drei Optionen.
            return max(res_pair, res_skip_i, res_skip_j)

        return solve(0, 0, k)
