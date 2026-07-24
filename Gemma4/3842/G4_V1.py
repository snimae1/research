class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        # Wir nutzen ein Set, um die Glühbirnen zu speichern, die gerade "an" sind.
        # Ein Set erlaubt uns einen schnellen Zugriff und einfachen Check, 
        # ob eine Birne bereits eingeschaltet ist.
        on_bulbs = set()

        for bulb in bulbs:
            if bulb in on_bulbs:
                # Wenn die Birne an ist, schalten wir sie aus (entfernen aus dem Set)
                on_bulbs.remove(bulb)
            else:
                # Wenn die Birne aus ist, schalten wir sie ein (hinzufügen zum Set)
                on_bulbs.add(bulb)

        # Am Ende geben wir die Liste der eingeschalteten Birnen 
        # aufsteigend sortiert zurück.
        return sorted(list(on_bulbs))
