class Solution(object):

    def compareBitonicSums(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Da das Array bitonisch ist (strikt steigend, dann strikt fallend),
        # ist das Peak-Element einfach das Maximum des Arrays.
        # Wir suchen den Index dieses Maximums.
        peak_index = 0
        for i in range(len(nums) - 1):
            if nums[i+1] > nums[i]:
                peak_index = i + 1
            else:
                # Sobald das nächste Element kleiner ist, haben wir den Peak erreicht.
                break
        
        # Berechnung der Summe des aufsteigenden Teils (Index 0 bis Peak inklusiv)
        ascending_sum = sum(nums[:peak_index + 1])
        
        # Berechnung der Summe des absteigenden Teils (Peak bis Ende inklusiv)
        descending_sum = sum(nums[peak_index:])
        
        # Vergleich der Summen gemäß den Anforderungen:
        # 0 if ascending > descending
        # 1 if descending > ascending
        # -1 if both are equal
        if ascending_sum > descending_sum:
            return 0
        elif descending_sum > ascending_sum:
            return 1
        else:
            return -1
