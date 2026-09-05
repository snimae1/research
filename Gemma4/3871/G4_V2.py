class Solution(object):

    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        total_commas = 0
        # Wir prüfen die Schwellenwerte für Kommas: 10^3, 10^6, 10^9, 10^12, 10^15...
        exponent = 3
        
        while True:
            threshold = 10**exponent
            if threshold > n:
                break
            
            # Die Anzahl der Zahlen im Bereich [1, n], die mindestens 'k' Kommas haben,
            # ist einfach (n - Schwellenwert + 1).
            total_commas += (n - threshold + 1)
            
            # Erhöhe den Exponenten um 3 für das nächste Komma
            exponent += 3
            
        return total_commas
