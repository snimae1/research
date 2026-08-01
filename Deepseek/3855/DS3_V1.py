class Solution(object):
    def sumOfNumbers(self, l, r, k):
        """
        :type l: int
        :type r: int
        :type k: int
        :rtype: int
        """
        MOD = 1000000007
        
        # Anzahl der gültigen Ziffern
        n = r - l + 1
        
        # Summe der gültigen Ziffern
        S = (l + r) * n // 2
        
        # Sonderfall: keine gültigen Ziffern (laut Constraints nicht möglich)
        if n == 0:
            return 0
        
        # n^(k-1) modulo MOD
        pow_n = pow(n, k - 1, MOD)
        
        # 10^k modulo MOD
        pow10 = pow(10, k, MOD)
        
        # Geometrische Reihe: (10^k - 1) / 9 modulo MOD
        inv9 = pow(9, MOD - 2, MOD)  # modulares Inverses von 9
        G = (pow10 - 1) * inv9 % MOD
        
        # Endergebnis berechnen
        ans = (S * pow_n) % MOD
        ans = (ans * G) % MOD
        
        return ans
