import math

class Solution(object):

    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        n = len(nums)
        prefixGcd = []
        mxi = 0
        
        # Schritt 1: Konstruktion von prefixGcd
        for i in range(n):
            # Aktualisiere das bisherige Maximum (mxi)
            if nums[i] > mxi:
                mxi = nums[i]
            
            # Berechne den GCD von nums[i] und dem aktuellen Maximum
            prefixGcd.append(math.gcd(nums[i], mxi))
        
        # Schritt 2: Sortiere prefixGcd in nicht-absteigender Reihenfolge
        prefixGcd.sort()
        
        # Schritt 3 & 4: Paare bilden (kleinstes mit größtem) und GCD-Summe berechnen
        total_gcd_sum = 0
        left = 0
        right = n - 1
        
        # Wir laufen von beiden Seiten zur Mitte. 
        # Wenn n ungerade ist, bleibt das mittlere Element (left == right) automatisch übrig.
        while left < right:
            total_gcd_sum += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_gcd_sum
