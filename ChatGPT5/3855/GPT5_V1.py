class Solution(object):
    def sumOfNumbers(self, l, r, k):
        """
        :type l: int
        :type r: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # Anzahl möglicher Ziffern
        m = r - l + 1

        # Summe aller erlaubten Ziffern
        digit_sum = (l + r) * m // 2

        # m^(k-1) mod MOD
        count = pow(m, k - 1, MOD)

        # 111...111 (k Einsen) = (10^k - 1) / 9
        # Iterativ berechnen:
        ones = 0
        p = 1
        n = k
        while n > 0:
            if n & 1:
                ones = (ones * pow(10, p, MOD) + self._repunit(p, MOD)) % MOD
            p <<= 1
            n >>= 1

        return (digit_sum % MOD) * count % MOD * ones % MOD

    def _repunit(self, length, MOD):
        """
        Gibt die Zahl 111...111 (length Einsen) modulo MOD zurück.
        Berechnung in O(log length).
        """
        if length == 0:
            return 0
        if length == 1:
            return 1

        if length % 2 == 0:
            half = self._repunit(length // 2, MOD)
            return (half * pow(10, length // 2, MOD) + half) % MOD
        else:
            return (self._repunit(length - 1, MOD) * 10 + 1) % MOD
