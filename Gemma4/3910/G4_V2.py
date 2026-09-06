"""
Dieses Modul enthält die Lösung für das Problem der verbundenen 
Subgraphen mit einer geraden Summe der Knotenwerte.
"""

class Solution:
    """
    Klasse zur Analyse von Graphen, um Teilmengen von Knoten zu finden,
    die zusammenhängend sind und eine gerade Summe ihrer Werte aufweisen.
    """

    def evenSumSubgraphs(self, nums, edges): # pylint: disable=invalid-name
        """
        Berechnet die Anzahl der nicht-leeren Teilmengen von Knoten,
        deren induzierter Subgraph zusammenhängend ist und dessen 
        Wertesumme gerade ist.

        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        # Erstellung der Adjazenzliste für effizienten Zugriff auf Nachbarn
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count = 0

        # Überprüfung aller 2^n - 1 möglichen nicht-leeren Teilmengen mittels Bitmasken
        for mask in range(1, 1 << n):
            subset = []
            current_sum = 0

            # Identifiziere Knoten, die in der aktuellen Bitmaske aktiviert sind
            for i in range(n):
                if (mask >> i) & 1:
                    subset.append(i)
                    current_sum += nums[i]

            # Bedingung 1: Die Summe der Knotenwerte muss gerade sein
            if current_sum % 2 == 0:
                # Bedingung 2: Der induzierte Subgraph muss zusammenhängend sein
                if self.is_connected(subset, adj):
                    count += 1

        return count

    def is_connected(self, subset, adj):
        """
        Prüft mittels einer Tiefensuche (DFS), ob eine gegebene 
        Knotenmenge im ursprünglichen Graphen zusammenhängend ist.

        :param subset: Liste der betrachteten Knoten
        :param adj: Adjazenzliste des Gesamtgraphen
        :return: True wenn zusammenhängend, sonst False
        """
        if not subset:
            return False

        # Startpunkt für die Traversierung
        start_node = subset[0]
        visited = {start_node}
        stack = [start_node]
        subset_set = set(subset)

        while stack:
            u = stack.pop()
            for v in adj[u]:
                # Nur Knoten besuchen, die Teil der aktuellen Teilmenge sind
                if v in subset_set and v not in visited:
                    visited.add(v)
                    stack.append(v)

        # Wenn alle Knoten der Teilmenge besucht wurden, ist sie zusammenhängend
        return len(visited) == len(subset)
