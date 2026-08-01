class Solution(object):

    def findValidElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [nums[0]]

        # Wir verwenden eine Liste von Booleans, um zu markieren, welche Elemente gültig sind.
        # Das erste und letzte Element sind laut Aufgabenstellung immer gültig.
        is_valid = [False] * n
        is_valid[0] = True
        is_valid[n - 1] = True

        # Bedingung 1: Streng größer als jedes Element links davon.
        # Wir gehen von links nach rechts und tracken das bisherige Maximum.
        current_max_left = nums[0]
        for i in range(1, n):
            if nums[i] > current_max_left:
                is_valid[i] = True
            # Update des Maximums für den nächsten Vergleich
            if nums[i] > current_max_left:
                current_max_left = nums[i]

        # Bedingung 2: Streng größer als jedes Element rechts davon.
        # Wir gehen von rechts nach links und tracken das bisherige Maximum.
        current_max_right = nums[n - 1]
        for i in range(n - 2, -1, -1):
            if nums[i] > current_max_right:
                is_valid[i] = True
            # Update des Maximums für den nächsten Vergleich
            if nums[i] > current_max_right:
                current_max_right = nums[i]

        # Erstelle die Ergebnisliste basierend auf den Markierungen in is_valid
        result = [nums[i] for i in range(n) if is_valid[i]]
        
        return result
