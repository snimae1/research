"""
Dieses Modul bietet eine Lösung zur Berechnung der Innenwinkel eines Dreiecks
basierend auf den gegebenen Seitenlängen.
"""

import math

class Solution:
    """
    Klasse zur Berechnungen von geometrischen Eigenschaften von Dreiecken.
    """

    # pylint: disable=invalid-name
    def internalAngles(self, sides):
        """
        Berechnet die Innenwinkel eines Dreiecks in aufsteigender Reihenfolge.

        :type sides: List[int]
        :rtype: List[float]
        """
        # 1. Sortieren der Seiten, um die Prüfung des Dreiecksungleichheitsgesetzes zu vereinfachen
        # Ein Dreieck existiert nur, wenn die Summe der zwei kürzesten Seiten
        # strikt größer ist als die längste Seite (a + b > c).
        s = sorted(sides)
        a, b, c = s[0], s[1], s[2]

        if a + b <= c:
            return []

        # 2. Berechnung der Winkel mittels Kosinussatz:
        # cos(A) = (b^2 + c^2 - a^2) / (2 * b * c)
        def calculate_angle(side1, side2, opposite_side):
            """Hilfsfunktion zur Berechnung eines einzelnen Winkels."""
            cos_val = (side1**2 + side2**2 - opposite_side**2) / (2 * side1 * side2)
            # math.acos liefert das Ergebnis in Radiant, math.degrees wandelt es in Grad um
            return math.degrees(math.acos(cos_val))

        # Wir berechnen alle drei Winkel
        angle1 = calculate_angle(b, c, a)
        angle2 = calculate_angle(a, c, b)
        angle3 = calculate_angle(a, b, c)

        # 3. Die Winkel in einer Liste speichern und aufsteigend sortieren
        result = sorted([angle1, angle2, angle3])

        return result

# pylint: disable=too-few-public-methods
