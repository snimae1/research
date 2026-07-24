from functools import lru_cache

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
        NEG_INF = float('-inf')

        @lru_cache(None)
        def dfs(i, j, rem):
            # Alle Paare gewählt
            if rem == 0:
                return 0

            # Nicht genügend Elemente übrig
            if n - i < rem or m - j < rem:
                return NEG_INF

            ans = NEG_INF

            # nums1[i] überspringen
            ans = max(ans, dfs(i + 1, j, rem))

            # nums2[j] überspringen
            ans = max(ans, dfs(i, j + 1, rem))

            # Beide koppeln
            ans = max(
                ans,
                nums1[i] * nums2[j] + dfs(i + 1, j + 1, rem - 1)
            )

            return ans

        return dfs(0, 0, k)
