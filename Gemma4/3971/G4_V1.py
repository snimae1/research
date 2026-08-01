class Solution(object):

    def maxTotalValue(self, value, decay, m):
        """
        :type value: List[int]
        :type decay: List[int]
        :type m: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        def get_count(X):
            """Berechnet, wie viele Selektionen einen Wert von mindestens X ergeben."""
            count = 0
            for v, d in zip(value, decay):
                if v >= X:
                    count += (v - X) // d + 1
            return count

        # Binäre Suche nach dem Schwellenwert 'threshold'
        # Wir suchen das größte X, sodass get_count(X) >= m.
        low = 1
        high = max(value) if value else 0
        threshold = 0
        
        while low <= high:
            mid = (low + high) // 2
            if get_count(mid) >= m:
                threshold = mid
                low = mid + 1
            else:
                high = mid - 1
        
        # Falls threshold == 0, bedeutet das, dass selbst bei X=1 nicht genug Elemente vorliegen.
        # Wir nehmen dann einfach alle positiven Werte.
        if threshold == 0:
            total_sum = 0
            for v, d in zip(value, decay):
                # Anzahl der positiven Terme für diesen Index
                k = (v - 1) // d + 1 if v > 0 else 0
                if k > 0:
                    # Summe einer arithmetischen Reihe: n/2 * (2a + (n-1)d)
                    # Hier ist der letzte Term a_k = v - (k-1)*d
                    total_sum += (k * (2 * v - (k - 1) * d)) // 2
            return total_sum % MOD

        # Wir nehmen alle Elemente, die STRIKT GRÖSSER als threshold sind.
        # Dann füllen wir den Rest bis m mit dem Wert 'threshold' auf.
        total_val = 0
        count_taken = 0
        X_plus_1 = threshold + 1
        
        for v, d in zip(value, decay):
            if v >= X_plus_1:
                k = (v - X_plus_1) // d + 1
                # Summe der ersten k Terme
                total_val += (k * (2 * v - (k - 1) * d)) // 2
                count_taken += k
        
        # Die verbleibenden Selektionen bis m werden mit dem Wert 'threshold' gefüllt
        remaining = m - count_taken
        total_val += remaining * threshold
        
        return total_val % MOD
