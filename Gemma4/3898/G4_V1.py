class Solution(object):

    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """ 
        # Wir nutzen eine List Comprehension, um durch jede Zeile der Matrix zu iterieren.
        # sum(row) zählt alle Einsen in der aktuellen Zeile, was genau dem Grad des Knotens entspricht.
        return [sum(row) for row in matrix]
