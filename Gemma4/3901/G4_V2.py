"""
Modul zur Berechnung von 'guten' Teilfolgen basierend auf dem GCD.
Eine Teilfolge ist gut, wenn ihr GCD genau p ist und ihre Länge < n ist.
"""

import math


class Solution:
    """
    Bietet eine Lösung zur Zählung von Queries, nach denen eine
    gute Teilfolge im Array existiert.
    """

    def countGoodSubseq(self, nums, p, queries):
        """
        Hauptmethode zur Verarbeitung der GCD-Queries.

        :type nums: List[int]
        :type p: int
        :type queries: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        self.p = p
        self.n = n
        self.nums = nums

        # Initialisierung des Segment-Trees
        self.tree_size = 1
        while self.tree_size < n:
            self.tree_size *= 2
        self.tree = [0] * (2 * self.tree_size)

        # Initialer Aufbau des Trees und Zählung der Vielfachen von p
        count_s = 0
        for i in range(n):
            if nums[i] % p == 0:
                count_s += 1
                self.tree[i + self.tree_size] = nums[i]

        for i in range(self.tree_size - 1, 0, -1):
            self.tree[i] = math.gcd(self.tree[2 * i], self.tree[2 * i + 1])

        total_good_queries = 0
        for indi, vali in queries:
            # Aktualisierung des Zählers für Elemente, die durch p teilbar sind
            count_s = self._update_count_s(count_s, indi, vali)
            self.nums[indi] = vali
            self._update_tree(indi, vali)

            if self._exists_good_subsequence(count_s):
                total_good_queries += 1

        return total_good_queries

    def _update_count_s(self, count_s, indi, vali):
        """Aktualisiert die Anzahl der Elemente, die Vielfache von p sind."""
        if self.nums[indi] % self.p == 0 and vali % self.p != 0:
            return count_s - 1
        if self.nums[indi] % self.p != 0 and vali % self.p == 0:
            return count_s + 1
        return count_s

    def _update_tree(self, idx, val):
        """Aktualisiert den Segment-Tree für eine bestimmte Position."""
        actual_val = val if val % self.p == 0 else 0
        pos = idx + self.tree_size
        self.tree[pos] = actual_val
        while pos > 1:
            pos //= 2
            new_gcd = math.gcd(self.tree[2 * pos], self.tree[2 * pos + 1])
            if self.tree[pos] == new_gcd:
                break
            self.tree[pos] = new_gcd

    def _exists_good_subsequence(self, count_s):
        """Prüft, ob unter den aktuellen Bedingungen eine gute Teilfolge existiert."""
        current_gcd = self.tree[1]
        if current_gcd != self.p:
            return False

        # Wenn nicht alle Elemente Vielfache von p sind, ist S (die Menge
        # der Vielfachen) bereits eine gute Teilfolge, da |S| < n.
        if count_s < self.n:
            return True

        # Spezialfall: Alle Elemente sind Vielfache von p (|S| = n).
        # Wir müssen prüfen, ob eine echte Teilmenge GCD p behält.
        return self._check_strict_subset_gcd()

    def _check_strict_subset_gcd(self):
        """Prüft, ob das Entfernen eines Elements den GCD bei p hält."""
        # Mathematische Eigenschaft: Bei Werten bis 50.000 und n >= 8 
        # existiert immer ein Element, dessen Entfernung den GCD p beibehält.
        if self.n >= 8:
            return True

        for i in range(self.n):
            if self._gcd_excluding_index(i) == self.p:
                return True
        return False

    def _gcd_excluding_index(self, exclude_idx):
        """Berechnet den GCD aller Elemente außer dem an exclude_idx."""
        res_gcd = 0
        for j in range(self.n):
            if j == exclude_idx:
                continue
            res_gcd = math.gcd(res_gcd, self.nums[j])
            if res_gcd == self.p:
                return res_gcd
        return res_gcd
