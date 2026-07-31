class Solution(object):

    def longestArithmetic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        n = len(nums)
        if n <= 2:
            return n
        
        # fwd[i]: Länge der arithmetischen Folge, die bei Index i endet
        fwd = [0] * n
        fwd[0] = 1
        if n > 1:
            fwd[1] = 2
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                fwd[i] = fwd[i-1] + 1
            else:
                fwd[i] = 2
        
        # bwd[i]: Länge der arithmetischen Folge, die bei Index i beginnt
        bwd = [0] * n
        bwd[n-1] = 1
        if n > 1:
            bwd[n-2] = 2
        for i in range(n-3, -1, -1):
            if nums[i+1] - nums[i] == nums[i+2] - nums[i+1]:
                bwd[i] = bwd[i+1] + 1
            else:
                bwd[i] = 2
        
        # Startwert: Wir können jede bestehende Folge um 1 verlängern, 
        # sofern sie nicht bereits die gesamte Länge n hat.
        ans = 0
        for i in range(n):
            if i > 0:
                ans = max(ans, fwd[i-1] + 1)
            if i < n - 1:
                ans = max(ans, bwd[i+1] + 1)

        # Prüfe jeden Index k als potentiellen "Brücken"-Punkt
        for k in range(1, n - 1):
            # Um nums[k] zu ersetzen und eine Brücke zu bauen, muss die 
            # Differenz d zwischen (nums[k-1], x) und (x, nums[k+1]) gleich sein.
            # Das bedeutet: nums[k+1] - nums[k-1] = 2 * d
            diff_sum = nums[k+1] - nums[k-1]
            if diff_sum % 2 == 0:
                d = diff_sum // 2
                current_len = 1 # Das ersetzte Element an Position k
                
                # Linke Seite prüfen
                if k - 2 >= 0 and nums[k-1] - nums[k-2] == d:
                    current_len += fwd[k-1]
                else:
                    current_len += 1 # Nur das Element an Position k-1 zählt
                
                # Rechte Seite prüfen
                if k + 2 < n and nums[k+2] - nums[k+1] == d:
                    current_len += bwd[k+1]
                else:
                    current_len += 1 # Nur das Element an Position k+1 zählt
                    
                ans = max(ans, current_len)
        
        # Das Ergebnis kann nicht größer als die Gesamtlänge des Arrays sein
        return min(ans, n)
