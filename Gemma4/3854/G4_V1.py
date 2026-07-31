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
