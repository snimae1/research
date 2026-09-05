"""
Dieses Modul enthält die Lösung für das Problem der Glühbirnen-Schalter.
Es implementiert eine Logik, um den Zustand von Glühbirnen basierend auf einer
Eingabeliste zu toggeln.
"""


class Solution:
    """
    Bietet Funktionen zum Verwalten des Zustands von 100 Glühbirnen.
    """

    def toggle_light_bulbs(self, bulbs):
        """
        Schaltet Glühbirnen basierend auf der Eingabeliste an und aus.

        :type bulbs: List[int]
        :rtype: List[int]
        """
        # Wir nutzen ein Set, um die Glühbirnen zu speichern, die gerade "an" sind.
        # Ein Set erlaubt uns einen schnellen Zugriff (O(1)).
        on_bulbs = set()

        for bulb in bulbs:
            self._toggle_bulb(on_bulbs, bulb)

        # Gibt die Liste der eingeschalteten Birnen aufsteigend sortiert zurück.
        return sorted(list(on_bulbs))

    def _toggle_bulb(self, bulb_set, bulb_id):
        """
        Hilfsmethode, um eine einzelne Glühbirne im Set umzuschalten.
        """
        if bulb_id in bulb_set:
            bulb_set.remove(bulb_id)
        else:
            bulb_set.add(bulb_id)
