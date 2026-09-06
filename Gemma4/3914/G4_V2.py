"""
Dieses Modul bietet eine Lösung, um die minimale Summe von Erhöhungen
zu berechnen, die erforderlich sind, um ein Array nicht-absteigend zu machen.
"""

# pylint: disable=too-few-public-methods
class Solution:
    """
    Klasse zur Berechnung der minimalen Operationen für ein nicht-absteigendes Array.
    """

    def min_operations(self, nums):
        """
        Berechnet die minimale Summe der Werte x, um das Array nicht-absteigend zu machen.

        :type nums: List[int]
        :rtype: int
        """
        total_x_sum = 0
        n = len(nums)

        for i in range(n - 1):
            # Wenn das aktuelle Element größer als das nächste ist,
            # muss die Differenz kompensiert werden.
            if nums[i] > nums[i + 1]:
                total_x_sum += nums[i] - nums[i + 1]

        return total_x_sum
