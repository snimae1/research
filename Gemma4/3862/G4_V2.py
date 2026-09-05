"""
Dieses Modul enthält die Lösung für das Problem des kleinsten balancierten Index.
Ein Index ist balanciert, wenn die Summe links gleich dem Produkt rechts ist.
"""

# pylint: disable=invalid-name
class Solution:
    """
    Klasse zur Berechnung des kleinsten balancierten Index in einer Liste von Zahlen.
    """

    def smallestBalancedIndex(self, nums):
        """
        Findet den kleinsten Index i, bei dem die Summe der Elemente links von i
        gleich dem Produkt der Elemente rechts von i ist.

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1

        # Berechnung der Suffix-Produkte (von rechts nach links).
        # suffix_products[i] speichert das Produkt aller Elemente ab Index i bis zum Ende.
        suffix_products = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_products[i] = nums[i] * suffix_products[i + 1]

        current_left_sum = 0

        # Durchlauf von links nach rechts, um den kleinsten Index zu finden.
        for i in range(n):
            # Das Produkt der Elemente streng rechts von i.
            right_product = suffix_products[i + 1]

            if current_left_sum == right_product:
                return i

            # Update der Summe für den nächsten Index.
            current_left_sum += nums[i]

        return -1
