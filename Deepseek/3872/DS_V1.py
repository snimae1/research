class Solution(object):
    def longestArithmetic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n
        
        # Unterschiede zwischen benachbarten Elementen
        diffs = [nums[i+1] - nums[i] for i in range(n-1)]
        m = len(diffs)  # m = n-1
        
        # Läufe gleicher Differenzen komprimieren
        runs = []  # (start_idx, end_idx, differenz, länge)
        i = 0
        while i < m:
            j = i
            while j < m and diffs[j] == diffs[i]:
                j += 1
            runs.append((i, j-1, diffs[i], j - i))
            i = j
        
        ans = 0
        
        for start, end, d, L in runs:
            # 1) Kein Ersatz
            ans = max(ans, L + 1)
            
            # 2) Erweiterung um 1 Element am Rand
            if start > 0:          # links
                ans = max(ans, L + 2)
            if end < m - 1:        # rechts (m-1 entspricht n-2)
                ans = max(ans, L + 2)
            
            # 3) Erweiterung um 2 Elemente auf einer Seite
            # links: Elemente start-2 und start-1 hinzufügen, start-1 ersetzen
            if start >= 2:
                if nums[start] - nums[start-2] == 2 * d:
                    ans = max(ans, L + 3)
            # rechts: Elemente end+2 und end+3 hinzufügen, end+2 ersetzen
            if end + 3 < n:
                if nums[end+3] - nums[end+1] == 2 * d:
                    ans = max(ans, L + 3)
        
        # 4) Zwei Läufe gleicher Differenz verbinden (Lücke genau 2 Differenzen)
        num_runs = len(runs)
        for i in range(num_runs):
            start1, end1, d, L1 = runs[i]
            
            # Lücke besteht aus einem Lauf der Länge 2
            if i + 2 < num_runs:
                mid = runs[i+1]
                right = runs[i+2]
                if right[2] == d and mid[3] == 2:
                    L2 = right[3]
                    # Bedingung: das mittlere Element ersetzen
                    if nums[end1+3] - nums[end1+1] == 2 * d:
                        ans = max(ans, L1 + L2 + 3)
            
            # Lücke besteht aus zwei Läufen der Länge 1
            if i + 3 < num_runs:
                mid1 = runs[i+1]
                mid2 = runs[i+2]
                right = runs[i+3]
                if right[2] == d and mid1[3] == 1 and mid2[3] == 1:
                    L2 = right[3]
                    if nums[end1+3] - nums[end1+1] == 2 * d:
                        ans = max(ans, L1 + L2 + 3)
        
        return ans
