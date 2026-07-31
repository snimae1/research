import math

class Solution(object):
    def isDigitorialPermutation(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Ziffern der ursprünglichen Zahl als Liste von Zeichen
        digits = list(str(n))
        
        # Summe der Fakultäten aller Ziffern berechnen
        s = sum(math.factorial(int(d)) for d in digits)
        
        # Ziffern der Summe als Liste von Zeichen
        sum_digits = list(str(s))
        
        # Prüfen, ob die Multimengen der Ziffern übereinstimmen
        return sorted(digits) == sorted(sum_digits)
