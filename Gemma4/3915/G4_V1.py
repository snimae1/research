class Solution(object):

    def maxAlternatingSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        
        # Coordinate Compression: Da die Werte in nums bis 10^5 gehen,
        # mappen wir sie auf ihren Rang (1 bis U), um sie im BIT zu nutzen.
        unique_sorted = sorted(list(set(nums)))
        rank = {val: i + 1 for i, val in enumerate(unique_sorted)}
        U = len(unique_sorted)

        # Fenwick-Baum (BIT) für Prefix-Maximumen
        class BIT:
            def __init__(self, size):
                self.tree = [0] * (size + 1)
            
            def update(self, i, val):
                while i < len(self.tree):
                    self.tree[i] = max(self.tree[i], val)
                    i += i & (-i)
            
            def query(self, i):
                res = 0
                while i > 0:
                    res = max(res, self.tree[i])
                    i -= i & (-i)
                return res

        # bit_down speichert Summen für Sequenzen, die gerade "unten" sind (Endwert klein)
        # Wir brauchen hier Prefix-Max für Werte < nums[i]
        bit_down = BIT(U)
        
        # bit_up speichert Summen für Sequenzen, die gerade "oben" sind (Endwert groß)
        # Wir brauchen hier Suffix-Max für Werte > nums[i]. 
        # Das erreichen wir durch Spiegelung des Index: rank -> U - rank + 1.
        bit_up = BIT(U)

        # dp_up[i]: max sum ending at index i, where nums[i] is a peak (or first element)
        # dp_down[i]: max sum ending at index i, where nums[i] is a valley (or first element)
        dp_up = [0] * n
        dp_down = [0] * n

        max_score = 0

        for i in range(n):
            # Wir können nur Elemente nutzen, die mindestens k Abstand zu i haben.
            # d.h. das Element an Index j = i - k wird jetzt erst "verfügbar".
            j = i - k
            if j >= 0:
                r_j = rank[nums[j]]
                bit_down.update(r_j, dp_down[j])
                # Spiegelung für Suffix-Query in bit_up
                bit_up.update(U - r_j + 1, dp_up[j])

            curr_val = nums[i]
            curr_rank = rank[curr_val]

            # Fall 1: Wir bilden eine Spitze (Peak). 
            # Wir suchen das beste "Tal" vor uns mit Wert < curr_val.
            best_prev_down = bit_down.query(curr_rank - 1)
            dp_up[i] = max(curr_val, best_prev_down + curr_val)

            # Fall 2: Wir bilden ein Tal (Valley). 
            # Wir suchen die beste "Spitze" vor uns mit Wert > curr_val.
            # Suffix Query over ranks [curr_rank + 1, U] -> Prefix Query over mirrored indices.
            best_prev_up = bit_up.query(U - curr_rank)
            dp_down[i] = max(curr_val, best_prev_up + curr_val)

            max_score = max(max_score, dp_up[i], dp_down[i])

        return max_score
