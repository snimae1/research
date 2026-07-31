class Solution(object):
    def sumOfNumbers(self, l, r, k):
        """
        :type l: int
        :type r: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # n ist die Anzahl der verfügbaren Ziffern pro Stelle
        n = r - l + 1
        
        # S ist die Summe aller verfügbaren Ziffern im Bereich [l, r]
        # Formel für Summe einer arithmetischen Reihe: (Anzahl * (Start + Ende)) / 2
        S = (n * (l + r)) // 2
        
        # Wir berechnen die Gesamtsumme nach der Formel:
        # Gesamt = S * n^(k-1) * (10^k - 1) / 9
        
        # Teil 1: S % MOD
        S_mod = S % MOD
        
        # Teil 2: n^(k-1) % MOD
        # Wir nutzen pow(base, exp, mod) für effizientes Modulo-Potenzieren (O(log k))
        n_pow = pow(n, k - 1, MOD)
        
        # Teil 3: (10^k - 1) / 9 % MOD
        # Die Division durch 9 wird durch Multiplikation mit dem modularen Inversen von 9 ersetzt.
        # Da MOD eine Primzahl ist, gilt nach dem kleinen Fermat: a^(p-2) % p ist das Inverse von a.
        ten_pow_k = pow(10, k, MOD)
        numerator = (ten_pow_k - 1 + MOD) % MOD
        inv_9 = pow(9, MOD - 2, MOD)
        geom_sum = (numerator * inv_9) % MOD
        
        # Alles zusammenführen
        result = (S_mod * n_pow) % MOD
        result = (result * geom_sum) % MOD
        
        return result
