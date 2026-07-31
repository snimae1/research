from collections import Counter

class Solution(object):
    def minCost(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # Gesamthäufigkeiten aller Elemente
        total_count = Counter(nums1) + Counter(nums2)
        
        # Wenn ein Element ungerade oft vorkommt, ist die Aufgabe unlösbar
        for count in total_count.values():
            if count % 2 != 0:
                return -1
        
        # Soll-Häufigkeit in jedem Array
        target = {val: cnt // 2 for val, cnt in total_count.items()}
        
        # Häufigkeit in nums1
        count1 = Counter(nums1)
        
        # Minimale Kosten = Anzahl der Elemente, die aus nums1 entfernt werden müssen
        swaps = 0
        for val, cnt in count1.items():
            if cnt > target[val]:
                swaps += cnt - target[val]
                
        return swaps
