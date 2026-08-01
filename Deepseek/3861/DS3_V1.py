class Solution(object):
    def minimumIndex(self, capacity, itemSize):
        """
        :type capacity: List[int]
        :type itemSize: int
        :rtype: int
        """
        min_capacity = float('inf')
        min_index = -1
        
        for i, cap in enumerate(capacity):
            if cap >= itemSize and cap < min_capacity:
                min_capacity = cap
                min_index = i
                
        return min_index
