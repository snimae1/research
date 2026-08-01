import math

class Solution(object):

    def countGoodSubseq(self, nums, p, queries):
        """
        :type nums: List[int]
        :type p: int
        :type queries: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        # Ein Segment-Tree zur Verwaltung des GCD der Elemente, die Vielfache von p sind.
        # Wir speichern im Tree den Wert, wenn nums[i] % p == 0, sonst 0.
        tree_size = 1
        while tree_size < n:
            tree_size *= 2
        
        tree = [0] * (2 * tree_size)

        def update_tree(idx, val):
            # Nur Werte speichern, die Vielfache von p sind
            actual_val = val if val % p == 0 else 0
            pos = idx + tree_size
            tree[pos] = actual_val
            while pos > 1:
                pos //= 2
                new_gcd = math.gcd(tree[2 * pos], tree[2 * pos + 1])
                if tree[pos] == new_gcd: 
                    break # Optimierung: Stoppen, wenn sich der Wert nicht ändert
                tree[pos] = new_gcd

        # Initialisierung des Trees und Zähler für Vielfache von p
        count_s = 0
        for i in range(n):
            if nums[i] % p == 0:
                count_s += 1
                # Manuelle Initialisierung zur Beschleunigung (keine recursive updates)
                tree[i + tree_size] = nums[i]
        
        for i in range(tree_size - 1, 0, -1):
            tree[i] = math.gcd(tree[2 * i], tree[2 * i + 1])

        ans = 0
        for indi, vali in queries:
            # Vorherigen Zustand prüfen für count_s
            if nums[indi] % p == 0 and vali % p != 0:
                count_s -= 1
            elif nums[indi] % p != 0 and vali % p == 0:
                count_s += 1
            
            nums[indi] = vali
            update_tree(indi, vali)
            
            current_gcd = tree[1]
            
            if current_gcd == p:
                # Fall 1: Nicht alle Elemente sind Vielfache von p
                if count_s < n:
                    ans += 1
                else:
                    # Fall 2: Alle Elemente sind Vielfache von p (S = nums)
                    # Wir müssen prüfen, ob eine echte Teilfolge mit GCD p existiert.
                    # Wenn n >= 8 und GCD(S)=p, gibt es immer eine solche Teilfolge bei max_val=50k.
                    if n >= 8:
                        ans += 1
                    else:
                        # Für kleine n prüfen wir alle Möglichkeiten (ein Element entfernen)
                        possible = False
                        for i in range(n):
                            # GCD aller Elemente außer Index i
                            # Wir nutzen hier eine einfache Methode, da n klein ist
                            temp_gcd = 0
                            for j in range(n):
                                if i == j: continue
                                temp_gcd = math.gcd(temp_gcd, nums[j])
                                if temp_gcd == p: break
                            if temp_gcd == p:
                                possible = True
                                break
                        if possible:
                            ans += 1
                            
        return ans
