from collections import Counter
from typing import List

class Solution(object):
    def minDistinctFreqPair(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = Counter(nums)
        # unique values present in nums, sorted ascending
        values = sorted(freq.keys())
        
        # Iterate over possible x in increasing order
        for i, x in enumerate(values):
            # For the current x, look for the smallest y > x with different frequency
            for y in values[i+1:]:
                if freq[y] != freq[x]:
                    return [x, y]
        
        # No valid pair found
        return [-1, -1]
