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
        
        # Falls kein stabiler Index gefunden wurde
        return -1
