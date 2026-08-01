class Solution(object):

    def sumOfPrimesInRange(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1. Den Umkehrwert r von n berechnen
        # Wir wandeln die Zahl in einen String um, drehen diesen um und konvertieren ihn zurück in ein Int
        r = int(str(n)[::-1])
        
        # 2. Die Grenzen des Bereichs bestimmen (min und max)
        start = min(n, r)
        end = max(n, r)
        
        # Hilfsfunktion zur Prüfung, ob eine Zahl prim ist
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
        
        # 3. Alle Primzahlen im Bereich [start, end] finden und summieren
        total_sum = 0
        for x in range(start, end + 1):
            if is_prime(x):
                total_sum += x
                
        return total_sum
