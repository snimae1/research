class Solution(object):

    def minAbsoluteDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        # Initialisierung des minimalen Abstands mit Unendlich
        min_diff = float('inf')
        
        # Variablen, um den letzten Index von 1 und 2 zu speichern
        last_one = -1
        last_two = -1

        for i in range(len(nums)):
            if nums[i] == 1:
                last_one = i
                # Wenn wir bereits eine 2 gefunden haben, berechne den Abstand
                if last_two != -1:
                    min_diff = min(min_diff, abs(i - last_two))
            
            elif nums[i] == 2:
                last_two = i
                # Wenn wir bereits eine 1 gefunden haben, berechne den Abstand
                if last_one != -1:
                    min_diff = min(min_diff, abs(i - last_one))

        # Wenn min_diff immer noch Unendlich ist, wurde kein gültiges Paar gefunden
        return min_diff if min_diff != float('inf') else -1
