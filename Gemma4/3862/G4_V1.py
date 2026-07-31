class Solution(object):

    def smallestBalancedIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        n = len(nums)
        if n == 0:
            return -1

        # Wir berechnen zuerst die Produkte von rechts nach links (Suffix-Produkte).
        # suffix_products[i] speichert das Produkt aller Elemente ab Index i bis zum Ende.
        suffix_products = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_products[i] = nums[i] * suffix_products[i+1]

        current_left_sum = 0
        
        # Wir gehen das Array von links nach rechts durch.
        # Da wir den kleinstmöglichen Index suchen, ist die erste Übereinstimmung unser Ergebnis.
        for i in range(n):
            # Gemäß Aufgabe: 
            # Links summe aller Elemente streng links von i.
            # Rechts produkt aller Elemente streng rechts von i.
            
            # Das Produkt der Elemente rechts von i finden wir in suffix_products[i+1]
            right_product = suffix_products[i + 1]

            if current_left_sum == right_product:
                return i
            
            # Update die Summe für den nächsten Index (das aktuelle Element kommt nun "links" vom nächsten i)
            current_left_sum += nums[i]

        return -1
