import math

class Solution(object):
    def internalAngles(self, sides):
        """
        :type sides: List[int]
        :rtype: List[float]
        """
        a, b, c = sides[0], sides[1], sides[2]
        
        # Check triangle inequality (strict for positive area)
        if a + b <= c or a + c <= b or b + c <= a:
            return []
        
        # Calculate angles using the law of cosines (in radians)
        angle_a = math.acos((b*b + c*c - a*a) / (2.0 * b * c))
        angle_b = math.acos((a*a + c*c - b*b) / (2.0 * a * c))
        angle_c = math.acos((a*a + b*b - c*c) / (2.0 * a * b))
        
        # Convert to degrees
        deg_a = angle_a * 180.0 / math.pi
        deg_b = angle_b * 180.0 / math.pi
        deg_c = angle_c * 180.0 / math.pi
        
        # Return sorted non-decreasing order
        return sorted([deg_a, deg_b, deg_c])
