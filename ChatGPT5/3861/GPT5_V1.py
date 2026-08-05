class Solution(object):
    def minimumIndex(self, capacity, itemSize):
        """
        :type capacity: List[int]
        :type itemSize: int
        :rtype: int
        """
        best_index = -1
        best_capacity = float('inf')

        for i in range(len(capacity)):
            if capacity[i] >= itemSize and capacity[i] < best_capacity:
                best_capacity = capacity[i]
                best_index = i

        return best_index
