class Solution(object):

    def maxValue(self, nums1, nums0):
        """
        :type nums1: List[int]
        :type nums0: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums1)
        
        # Wir teilen die Segmente in drei Kategorien ein, um die maximale 
        # binäre Zahl zu konstruieren.
        pure_ones = []    # Nur Einsen (z == 0)
        mixed = []        # Sowohl Einsen als auch Nullen (o > 0 und z > 0)
        pure_zeros = []   # Nur Nullen (o == 0)
        
        for i in range(n):
            o, z = nums1[i], nums0[i]
            if z == 0:
                pure_ones.append((o, z))
            elif o == 0:
                pure_zeros.append((o, z))
            else:
                mixed.append((o, z))
        
        # Sortierung für gemischte Segmente:
        # 1. Anzahl der Einsen absteigend (mehr '1's vorne)
        # 2. Anzahl der Nullen aufsteigend (weniger Lücken zwischen den Blöcken)
        mixed.sort(key=lambda x: (-x[0], x[1]))
        
        # Die optimale Reihenfolge ist: Pure Einsen -> Sortierte Gemischte -> Pure Nullen
        final_order = pure_ones + mixed + pure_zeros
        
        ans = 0
        for o, z in final_order:
            # Ein Segment besteht aus 'o' Einsen gefolgt von 'z' Nullen.
            # Wert eines Segments allein: (2^o - 1) * 2^z
            # Gesamtwert-Update: ans = (ans * 2^(o+z)) + segment_value
            
            length = o + z
            if length == 0: continue # Sicherheitshalber, falls ein Segment leer ist
            
            # Verschiebe den aktuellen Wert um die Länge des neuen Segments nach links
            ans = (ans * pow(2, length, MOD)) % MOD
            
            # Berechne den Wert der Einsen im aktuellen Segment: 
            # Beispiel: "110" bei o=2, z=1 -> (2^2 - 1) * 2^1 = 3 * 2 = 6
            segment_val = ((pow(2, o, MOD) - 1) * pow(2, z, MOD)) % MOD
            
            ans = (ans + segment_val) % MOD
            
        return ans
