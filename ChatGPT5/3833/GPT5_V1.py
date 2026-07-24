class Solution(object):
    def dominantIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Das letzte Element kann nie dominant sein.
        if n == 1:
            return 0
        
        # Suffixsumme berechnen
        suffix_sum = sum(nums)
        count = 0
        
        for i in range(n - 1):
            suffix_sum -= nums[i]  # Summe der Elemente rechts von i
            right_count = n - i - 1
            
            # nums[i] > Durchschnitt der rechten Elemente
            # Multiplikation vermeidet Fließkommazahlen:
            if nums[i] * right_count > suffix_sum:
                count += 1
        
        return count
