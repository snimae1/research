"""Module providing a solution for calculating triangle internal angles."""
import math


class Solution:
    """Solution class for the triangle angles problem."""
    # pylint: disable=too-few-public-methods

    def internalAngles(self, sides):
        # pylint: disable=invalid-name
        """
        Return the internal angles of a triangle with given side lengths.

        :type sides: List[int]
        :rtype: List[float]
        """
        a, b, c = sides

        # Check triangle inequality for positive area
        if a + b <= c or a + c <= b or b + c <= a:
            return []

        # Compute angles using the law of cosines
        angle_a = math.degrees(math.acos((b * b + c * c - a * a) / (2.0 * b * c)))
        angle_b = math.degrees(math.acos((a * a + c * c - b * b) / (2.0 * a * c)))
        angle_c = math.degrees(math.acos((a * a + b * b - c * c) / (2.0 * a * b)))

        return sorted([angle_a, angle_b, angle_c])
