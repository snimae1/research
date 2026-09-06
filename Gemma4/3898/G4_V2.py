"""
Dieses Modul enthält die Klasse Solution, welche Funktionen zur
Analyse von Graphen bereitstellt, speziell die Berechnung von Knotengraden.
"""

class Solution:
    """
    Bietet Methoden zur Berechnung von Graphen-Metriken basierend auf 
    einer Adjazenzmatrix.
    """

    def find_degrees(self, matrix):
        """
        Berechnet den Grad jedes Knotens in einem ungerichteten Graphen.

        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Die Summe einer Zeile in der Adjazenzmatrix entspricht dem Knotengrad.
        return [sum(row) for row in matrix]
