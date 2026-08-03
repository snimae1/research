class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        # Set für die aktuell eingeschalteten Lampen
        on = set()
        
        for b in bulbs:
            if b in on:
                on.remove(b)   # War an → ausschalten
            else:
                on.add(b)      # War aus → einschalten
                
        # Sortierte Liste der eingeschalteten Lampen zurückgeben
        return sorted(on)
