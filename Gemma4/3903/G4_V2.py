"""
Dieses Modul bietet eine Lösung zur Berechnung des ersten stabilen Index
eines Arrays basierend auf einem Instabilitäts-Score.
"""

# pylint: disable=too-few-public-methods
class Solution:
    """
    Klasse zur Lösung des Problems der Instabilitäts-Scores.
    """

    def first_stable_index(self, nums, k):
        """
        Findet den kleinsten Index i, bei dem max(nums[0..i]) - min(nums[i..n-1]) <= k.

        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1

        # prefix_max[i] speichert den größten Wert von index 0 bis i
        prefix_max = [0] * n
        current_max = float('-inf')
        for i in range(n):
            current_max = max(current_max, nums[i])
            prefix_max[i] = current_max

        # suffix_min[i] speichert den kleinsten Wert von index i bis n-1
        suffix_min = [0] * n
        current_min = float('inf')
        for i in range(n - 1, -1, -1):
            current_min = min(current_min, nums[i])
            suffix_min[i] = current_min

        # Überprüfe für jeden Index i den Instabilitäts-Score
        for i in range(n):
            instability_score = prefix_max[i] - suffix_min[i]
            if instability_score <= k:
                return i

        return -1
