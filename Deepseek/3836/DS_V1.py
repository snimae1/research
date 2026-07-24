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
        NEG_INF = -10**18

        # dp[t][i][j] = maximale Punktzahl, wenn wir aus den ersten i Elementen von nums1
        # und den ersten j Elementen von nums2 genau t Paare ausgewählt haben.
        dp = [[[NEG_INF] * (m + 1) for _ in range(n + 1)] for __ in range(k + 1)]

        # Für t = 0 ist die Punktzahl immer 0, unabhängig davon, wie viele Elemente betrachtet wurden.
        for i in range(n + 1):
            for j in range(m + 1):
                dp[0][i][j] = 0

        # Dynamische Programmierung
        for t in range(1, k + 1):
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    # Möglichkeit 1: nums1[i-1] wird nicht verwendet
                    best = dp[t][i-1][j]

                    # Möglichkeit 2: nums2[j-1] wird nicht verwendet
                    if dp[t][i][j-1] > best:
                        best = dp[t][i][j-1]

                    # Möglichkeit 3: nums1[i-1] und nums2[j-1] werden als t‑tes Paar verwendet
                    if dp[t-1][i-1][j-1] != NEG_INF:
                        candidate = dp[t-1][i-1][j-1] + nums1[i-1] * nums2[j-1]
                        if candidate > best:
                            best = candidate

                    dp[t][i][j] = best

        return dp[k][n][m]
