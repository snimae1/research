import math

class Solution(object):
    def isDigitorialPermutation(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Vorbereiten der Fakultäten für Ziffern 0-9 (für bessere Performance)
        # 0! = 1, 1! = 1, 2! = 2, ..., 9! = 362880
        fact = [math.factorial(i) for i in range(10)]
        
        # Schritt 1: Die Ziffern von n extrahieren
        str_n = str(n)
        digits_n = [int(d) for d in str_n]
        
        # Schritt 2: die Summe der Fakultäten aller Ziffern berechnen.
        # Diese Summe ist für jede beliebige Permutation von n identisch.
        sum_of_factorials = sum(fact[d] for d in digits_n)
        
        # Schritt 3: Prüfen, ob die resultierende Summe eine gültige Permutation von n ist.
        # Eine Zahl ist eine gültige Permutation einer anderen, wenn:
        # a) Sie dieselben Ziffern in derselben Anzahl enthält.
        # b) Sie nicht mit Null beginnt (die Python-Umwandlung str(int) 
        #    erzeugt automatisch keine führenden Nullen).
        
        str_sum = str(sum_of_factorials)
        
        # Vergleiche die sortierten Ziffern beider Zahlen.
        # Wenn sie identisch sind, ist sum_of_factorials eine Permutation von n.
        return sorted(str_n) == sorted(str_sum)
