"""Berechnung der Innenwinkel eines Dreiecks anhand seiner Seitenlängen."""

import math


class Solution:
    """Löst die Aufgabe zur Bestimmung der Innenwinkel eines Dreiecks."""

    def internalAngles(self, sides):  # pylint: disable=invalid-name
        """
        Berechnet die drei Innenwinkel eines gültigen Dreiecks.

        :type sides: List[int]
        :rtype: List[float]
        """
        smallest, middle, largest = sorted(sides)

        # Ein Dreieck mit positiver Fläche muss die Dreiecksungleichung erfüllen.
        if smallest + middle <= largest:
            return []

        def calculate_angle(opposite, adjacent_one, adjacent_two):
            """Berechnet einen Winkel mithilfe des Kosinussatzes."""
            cosine = (
                adjacent_one ** 2
                + adjacent_two ** 2
                - opposite ** 2
            ) / (2.0 * adjacent_one * adjacent_two)

            # Schutz gegen minimale Fließkomma-Ungenauigkeiten.
            cosine = max(-1.0, min(1.0, cosine))

            return math.degrees(math.acos(cosine))

        angles = [
            calculate_angle(smallest, middle, largest),
            calculate_angle(middle, smallest, largest),
            calculate_angle(largest, smallest, middle),
        ]

        return sorted(angles)
