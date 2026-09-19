#Der gesamte von Gemma erstellte Code für die Aufgabe.
#Wobei eigentlich ja nur die zweite hälfte mit der richtigen Syntax gefordert war.

class Solution(object):
    def makeParityAlternating(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 1:
            return [0, 0]

        def solve_for_pattern(start_parity):
            # start_parity: 0 for even, 1 for odd
            fixed = []
            changed = [] # list of (low, high) where low = x-1 and high = x+1
            ops = 0
            
            for i in range(n):
                target_parity = (start_parity + i) % 2
                if nums[i] % 2 == target_parity:
                    fixed.append(nums[i])
                else:
                    ops += 1
                    changed.append((nums[i] - 1, nums[i] + 1))
            
            # Berechnung des minimalen Ranges für dieses Muster
            if not changed:
                return ops, max(fixed) - min(fixed)
            
            # Sortiere die 'low'-Werte der zu ändernden Elemente
            changed.sort() 
            
            # Vorbereiten von Prefix-Max (Highs) und Suffix-Max (Lows)
            m = len(changed)
            pre_max_high = [-float('inf')] * (m + 1)
            for i in range(m):
                pre_max_high[i+1] = max(pre_max_high[i], changed[i][1])
                
            suf_max_low = [-float('inf')] * (m + 1)
            for i in range(m - 1, -1, -1):
                suf_max_low[i] = max(suf_max_low[i+1], changed[i][0])
            
            # Grenzen für das mögliche Minimum M
            # M muss kleiner oder gleich allen 'high' Werten sein und <= min(fixed)
            limit = min(c[1] for c in changed)
            if fixed:
                limit = min(limit, min(fixed))
            
            max_fixed = max(fixed) if fixed else -float('inf')
            
            min_range = float('inf')
            
            # Wir testen mögliche Werte für M. 
            # Die optimalen M-Werte liegen entweder bei einem 'low'-Wert oder am limit.
            candidates = [c[0] for c in changed] + [limit]
            
            import bisect
            for M in candidates:
                if M > limit:
                    continue
                
                # Finde, welche Elemente zwingend auf 'high' springen müssen (low < M)
                # Da 'changed' sortiert ist, sind dies die Indizes 0 bis k-1
                k = bisect.bisect_left([c[0] for c in changed], M)
                
                # Das aktuelle Maximum des Arrays bei diesem M:
                current_max = max(max_fixed, pre_max_high[k], suf_max_low[k])
                
                # Range ist max(M, current_max) - M
                min_range = min(min_range, max(M, current_max) - M)
                
            return ops, min_range

    def makeParityAlternating(self, nums):
        # Wir prüfen beide Start-Muster (Even / Odd)
        res0_ops, res0_range = self.solve_for_pattern_internal(nums, 0)
        res1_ops, res1_range = self.solve_for_pattern_internal(nums, 1)
        
        min_ops = min(res0_ops, res1_ops)
        
        if res0_ops == res1_ops:
            return [min_ops, min(res0_range, res1_range)]
        elif res0_ops < res1_ops:
            return [min_ops, res0_range]
        else:
            return [min_ops, res1_range]

    # Hilfsfunktion, da die Syntax der Klasse Solution strikt eingehalten werden muss
    def solve_for_pattern_internal(self, nums, start_parity):
        n = len(nums)
        fixed = []
        changed = [] 
        ops = 0
        for i in range(n):
            target_parity = (start_parity + i) % 2
            if nums[i] % 2 == target_parity:
                fixed.append(nums[i])
            else:
                ops += 1
                changed.append((nums[i] - 1, nums[i] + 1))
        
        if not changed:
            return ops, (max(fixed) - min(fixed) if fixed else 0)
            
        changed.sort()
        m = len(changed)
        pre_max_high = [-float('inf')] * (m + 1)
        for i in range(m): pre_max_high[i+1] = max(pre_max_high[i], changed[i][1])
        suf_max_low = [-float('inf')] * (m + 1)
        for i in range(m - 1, -1, -1): suf_max_low[i] = max(suf_max_low[i+1], changed[i][0])
        
        limit = min(c[1] for c in changed)
        if fixed: limit = min(limit, min(fixed))
        max_fixed = max(fixed) if fixed else -float('inf')
        
        min_range = float('inf')
        # Optimierung: Nur relevante M testen
        candidates = [c[0] for c in changed] + [limit]
        lows_only = [c[0] for c in changed]
        
        import bisect
        for M in candidates:
            if M > limit: continue
            k = bisect.bisect_left(lows_only, M)
            current_max = max(max_fixed, pre_max_high[k], suf_max_low[k])
            min_range = min(min_range, max(M, current_max) - M)
            
        return ops, int(min_range)

# Um die Syntax aus der Aufgabe exakt einzuhalten:
class Solution(object):
    def makeParityAlternating(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 1: return [0, 0]

        def get_metrics(start_parity):
            fixed = []
            changed = []
            ops = 0
            for i in range(n):
                tp = (start_parity + i) % 2
                if nums[i] % 2 == tp: fixed.append(nums[i])
                else:
                    ops += 1
                    changed.append((nums[i]-1, nums[i]+1))
            
            if not changed: return ops, (max(fixed) - min(fixed) if fixed else 0)
            
            changed.sort()
            m = len(changed)
            pre_h = [-float('inf')] * (m + 1)
            for i in range(m): pre_h[i+1] = max(pre_h[i], changed[i][1])
            suf_l = [-float('inf')] * (m + 1)
            for i in range(m-1, -1, -1): suf_l[i] = max(suf_l[i+1], changed[i][0])
            
            lim = min(c[1] for c in changed)
            if fixed: lim = min(lim, min(fixed))
            max_f = max(fixed) if fixed else -float('inf')
            
            cur_min_range = float('inf')
            lows = [c[0] for c in changed]
            for M in lows + [lim]:
                if M > lim: continue
                import bisect
                k = bisect.bisect_left(lows, M)
                cur_max = max(max_f, pre_h[k], suf_l[k])
                cur_min_range = min(cur_min_range, max(M, cur_max) - M)
            return ops, int(cur_min_range)

        o0, r0 = get_metrics(0)
        o1, r1 = get_metrics(1)
        
        if o0 < o1: return [o0, r0]
        if o1 < o0: return [o1, r1]
        return [o0, min(r0, r1)]
