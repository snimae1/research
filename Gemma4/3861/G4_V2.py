"""
Dieses Modul bietet eine Lösung, um die Box mit der kleinstmöglichen 
Kapazität zu finden, die ein Objekt einer bestimmten Größe aufnehmen kann.
"""

# pylint: disable=too-few-public-methods
class Solution:
    """
    Klasse zur Berechnung des minimalen Index einer passenden Box.
    """

    def minimum_index(self, capacity, item_size):
        """
        Findet den Index der Box mit der kleinsten Kapazität, die >= item_size ist.

        :type capacity: List[int]
        :type item_size: int
        :rtype: int
        """
        # Variable für den Index der besten Box (initial -1, falls keine gefunden wird)
        min_index = -1
        # Variable für die bisher gefundene kleinste passende Kapazität (initial Unendlich)
        min_cap = float('inf')

        # Verwendung von enumerate statt range(len()), wie von Pylint empfohlen
        for i, current_cap in enumerate(capacity):
            # Prüfen, ob das Item überhaupt in die Box passt
            if current_cap >= item_size:
                # Wir suchen die MINIMALE Kapazität.
                # Da wir den kleinsten Index bei Gleichstand wollen,
                # nutzen wir den strikten Vergleich '<'.
                if current_cap < min_cap:
                    min_cap = current_cap
                    min_index = i

        return min_index
