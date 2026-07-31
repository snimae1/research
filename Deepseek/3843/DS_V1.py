from typing import List
from collections import Counter

class Solution(object):
    def firstUniqueFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Häufigkeiten aller Zahlen zählen
        freq = Counter(nums)
        
        # Zählen, wie oft jede Häufigkeit vorkommt
        freq_count = Counter(freq.values())
        
        # Von links nach rechts prüfen
        for num in nums:
            if freq_count[freq[num]] == 1:
                return num
        
        # Kein Element mit eindeutiger Häufigkeit gefunden
        return -1
