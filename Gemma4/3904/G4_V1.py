class Solution(object):

    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """ 
        n = len(nums)
        if n == 0:
            return -1
        
        # Schritt 1: Berechne das Minimum für jeden Suffix [i...n-1]
        # Wir erstellen ein Array, in dem suffix_min[i] den kleinsten Wert 
        # von Index i bis zum Ende der Liste speichert.
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
            
        # Schritt 2: Iteriere durch die Liste und tracke das laufende Maximum (Präfix)
        # Wir berechnen gleichzeitig den instability score für jeden Index i.
        current_max = float('-inf')
        for i in range(n):
            # Update des Maximums von nums[0...i]
            if nums[i] > current_max:
                current_max = nums[i]
            
            # Instability Score = max(nums[0..i]) - min(nums[i..n-1])
            instability_score = current_max - suffix_min[i]
            
            # Prüfen, ob der Index stabil ist
            if instability_score <= k:
                return i
        
        # Falls kein stabiler Index gefunden wurde
        return -1
