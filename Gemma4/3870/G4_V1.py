class Solution(object):

    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        total_commas = 0
        # Ein Komma erscheint alle 3 Stellen von rechts.
        # Zahlen von 1.000 bis 999.999 haben 1 Komma.
        # Zahlen von 1.000.000 bis 999.999.999 haben 2 Kommas, usw.
        
        # Wir iterieren über die Schwellenwerte (10^3, 10^6, 10^9...)
        k = 1
        while True:
            lower_bound = 10**(3 * k)
            if lower_bound > n:
                break
            
            upper_bound = 10**(3 * (k + 1)) - 1
            # Wir berechnen, wie viele Zahlen im Bereich [lower_bound, upper_bound] 
            # bis maximal 'n' existieren.
            count_in_range = min(n, upper_bound) - lower_bound + 1
            
            # Jede Zahl in diesem Bereich hat mindestens k Kommas.
            total_commas += count_in_range * k
            k += 1
            
        return total_commas
