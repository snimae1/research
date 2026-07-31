class Solution(object):

    def minimumIndex(self, capacity, itemSize):
        """
        :type capacity: List[int]
        :type itemSize: int
        :rtype: int
        """ 
        # Variable für den Index der besten Box (initial -1, falls keine gefunden wird)
        minIndex = -1
        # Variable für die bisher gefundene kleinste passende Kapazität (initial Unendlich)
        minCap = float('inf')

        for i in range(len(capacity)):
            current_cap = capacity[i]
            
            # Prüfen, ob das Item überhaupt in die Box passt
            if current_cap >= itemSize:
                # Wir suchen die MINIMALE Kapazität.
                # Da wir den kleinsten Index bei Gleichstand wollen, 
                # nutzen wir den strikten Vergleich '<'. 
                # Nur wenn die aktuelle Box kleiner ist als die bisherige beste, ändern wir den Index.
                if current_cap < minCap:
                    minCap = current_cap
                    minIndex = i

        return minIndex
