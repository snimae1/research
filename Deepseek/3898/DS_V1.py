class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Der Grad eines Knotens i ist die Summe der i-ten Zeile der Adjazenzmatrix.
        # Da der Graph ungerichtet ist und keine Schleifen (matrix[i][i] == 0) existieren,
        # zählt jedes matrix[i][j] == 1 genau eine Kante zwischen i und j.
        return [sum(row) for row in matrix]
