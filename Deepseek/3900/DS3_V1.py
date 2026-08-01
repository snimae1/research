class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # Total counts of zeros and ones in the whole string
        total0 = s.count('0')
        total1 = n - total0

        # --- 1. Longest balanced substring without any swap (sum = 0) ---
        max0 = 0
        first = {0: 0}
        p = 0
        for j, ch in enumerate(s, 1):
            p += 1 if ch == '1' else -1
            if p in first:
                max0 = max(max0, j - first[p])
            else:
                first[p] = j

        # --- 2. Longest substring that becomes balanced after fixing sum = 2 ---
        max2 = 0
        first_all = {0: 0}
        first_posZ = {}          # only starts with zeros > 0
        p = 0
        z = 0
        for j, ch in enumerate(s, 1):
            if ch == '1':
                p += 1
            else:
                p -= 1
                z += 1
            target = p - 2
            # Case A: the start index has Z[i] > 0
            if target in first_posZ:
                max2 = max(max2, j - first_posZ[target])
            # Case B: the end index has Z[j] < total0
            if z < total0 and target in first_all:
                max2 = max(max2, j - first_all[target])

            # Update structures with current index as a future start
            if p not in first_all:
                first_all[p] = j
            if z > 0 and p not in first_posZ:
                first_posZ[p] = j

        # --- 3. Longest substring that becomes balanced after fixing sum = -2 ---
        max_neg2 = 0
        first_all2 = {0: 0}
        first_posO = {}          # only starts with ones > 0
        p = 0
        o = 0
        for j, ch in enumerate(s, 1):
            if ch == '1':
                p += 1
                o += 1
            else:
                p -= 1
            target = p + 2
            # Case A: the start index has O[i] > 0
            if target in first_posO:
                max_neg2 = max(max_neg2, j - first_posO[target])
            # Case B: the end index has O[j] < total1
            if o < total1 and target in first_all2:
                max_neg2 = max(max_neg2, j - first_all2[target])

            if p not in first_all2:
                first_all2[p] = j
            if o > 0 and p not in first_posO:
                first_posO[p] = j

        return max(max0, max2, max_neg2)
