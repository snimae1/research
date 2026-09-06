"""Lösung für die Berechnung der Knotengrade aus einer Adjazenzmatrix."""


class Solution(object):
    """Klasse zur Berechnung der Grade eines ungerichteten Graphen."""

    def findDegrees(self, matrix):
        """
        Berechnet die Grade aller Knoten.

        :param matrix: Adjazenzmatrix des Graphen (List[List[int]])
        :return: Liste der Grade (List[int])
        """
        # Der Grad eines Knotens i ist die Summe der i-ten Zeile.
        # Da der Graph ungerichtet und ohne Schleifen ist,
        # entspricht jede 1 einer Kante zu einem anderen Knoten.
        return [sum(row) for row in matrix]
