import math

class Solution(object):
    def internalAngles(self, sides):
        """
        :type sides: List[int]
        :rtype: List[float]
        """
        a, b, c = sorted(sides)

        # Dreiecksungleichung prüfen
        if a + b <= c:
            return []

        # Kosinussatz zur Berechnung der Winkel
        def angle(opposite, side1, side2):
            cos_value = (
                (side1 * side1 + side2 * side2 - opposite * opposite)
                / (2.0 * side1 * side2)
            )

            # Numerische Rundungsfehler vermeiden
            cos_value = max(-1.0, min(1.0, cos_value))

            return math.degrees(math.acos(cos_value))

        angle_a = angle(a, b, c)
        angle_b = angle(b, a, c)
        angle_c = angle(c, a, b)

        return sorted([angle_a, angle_b, angle_c])
