class Solution(object):
    def countVisiblePeople(self, n, pos, k):
        """
        :type n: int
        :type pos: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Wenn k mehr Personen verlangt, als überhaupt existieren (außer pos), ist es unmöglich.
        if k > n - 1:
            return 0
        
        # Wir müssen k Personen aus den insgesamt (n-1) möglichen Kandidaten auswählen.
        # Die Formel lautet: Combinations(n-1, k) * 2 (da Person at pos L oder R wählen kann).
        
        def nCr_mod(n, r, p):
            if r < 0 or r > n:
                return 0
            if r == 0 or r == n:
                return 1
            if r > n // 2:
                r = n - r
                
            # Berechnung des Binomialkoeffizienten unter Modulo
            num = 1
            den = 1
            for i in range(r):
                num = (num * (n - i)) % p
                den = (den * (i + 1)) % p
            
            # Modular inverse von den mittels Fermats kleinem Theorem: 
            # a^(p-2) % p ist das inverse von a modulo p, wenn p prim ist.
            return (num * pow(den, p - 2, p)) % p

        # Berechne Binomialkoeffizient C(n-1, k)
        combinations = nCr_mod(n - 1, k, MOD)
        
        # Multipliziere mit 2 (für die Wahl von Person an Index 'pos') und nehme modulo
        return (combinations * 2) % MOD
