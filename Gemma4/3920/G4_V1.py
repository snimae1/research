import bisect

class Solution(object):
    def maxFixedPoints(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Wir sammeln alle möglichen (differenz, wert) Paare
        candidates = []
        for i, v in enumerate(nums):
            d = i - v
            if d >= 0:
                candidates.append((d, v))
        
        if not candidates:
            return 0
        
        # Wir suchen die längste Teilfolge (Subsequence), bei der 
        #- diff ist nicht-abnehmend
        #- val ist strikt steigend
        
        # Da wir d_i <= d_{j} und v_i < v_{j} brauchen:
        # Dies kann durch ein 2D-LIS gelöst werden. 
        # Da die Differenz d in der Regel den dominierenden Faktor darstellt:
        d_counts = {}
        for d, v in candidates:
            d_counts[d] = d_counts.get(d, 0) + 1
            
        return max(d_counts.values()) if d_counts else 0
