"""
Module for solving the maximum score problem with two arrays and k pairs.
"""

class Solution:
    """
    Provides a method to compute the maximum total score by selecting exactly k
    pairs of indices with strictly increasing indices from two arrays.
    """

    def maxScore(self, nums1, nums2, k):
        # pylint: disable=invalid-name
        """
        Returns the maximum achievable total score.

        Args:
            nums1: List[int] of length n.
            nums2: List[int] of length m.
            k: int, number of pairs to select.

        Returns:
            int: maximum total score.
        """
        n = len(nums1)
        m = len(nums2)
        neg_inf = -10**18

        # dp_prev[i][j] represents the best score for t-1 pairs using
        # first i elements of nums1 and first j elements of nums2.
        dp_prev = [[neg_inf] * (m + 1) for _ in range(n + 1)]
        # For t = 0, score is 0 regardless of prefix lengths.
        for i in range(n + 1):
            for j in range(m + 1):
                dp_prev[i][j] = 0

        # Iterate over number of chosen pairs.
        for t in range(1, k + 1):
            dp_cur = [[neg_inf] * (m + 1) for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    # Option 1: skip nums1[i-1]
                    best = dp_cur[i-1][j]
                    # Option 2: skip nums2[j-1]
                    best = max(best, dp_cur[i][j-1])
                    # Option 3: use both nums1[i-1] and nums2[j-1] as the t-th pair
                    if dp_prev[i-1][j-1] != neg_inf:
                        candidate = dp_prev[i-1][j-1] + nums1[i-1] * nums2[j-1]
                        best = max(best, candidate)
                    dp_cur[i][j] = best
            dp_prev = dp_cur

        return dp_prev[n][m]
