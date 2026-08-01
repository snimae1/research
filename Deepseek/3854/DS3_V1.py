class Solution(object):
    def makeParityAlternating(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return [0, 0]
        
        # mismatches[0] for pattern: even at even indices, odd at odd indices
        # mismatches[1] for pattern: odd at even indices, even at odd indices
        mismatches = [0, 0]
        for i, num in enumerate(nums):
            parity = num % 2
            for p in (0, 1):
                desired = (i % 2) ^ p
                if parity != desired:
                    mismatches[p] += 1
        
        k = min(mismatches)
        
        def min_range_for_pattern(pattern):
            fixed = []
            free = []
            for i, num in enumerate(nums):
                desired = (i % 2) ^ pattern
                if num % 2 == desired:
                    fixed.append(num)
                else:
                    free.append(num)
            
            if not free:
                if not fixed:
                    return 0
                return max(fixed) - min(fixed)
            
            fixed.sort()
            free.sort()
            m = len(free)
            
            free_plus = [x + 1 for x in free]
            free_minus = [x - 1 for x in free]
            
            # prefix max/min for free_plus
            pref_max_plus = [float('-inf')] * m
            pref_min_plus = [float('inf')] * m
            pref_max_plus[0] = free_plus[0]
            pref_min_plus[0] = free_plus[0]
            for i in range(1, m):
                pref_max_plus[i] = max(pref_max_plus[i-1], free_plus[i])
                pref_min_plus[i] = min(pref_min_plus[i-1], free_plus[i])
            
            # suffix max/min for free_minus
            suff_max_minus = [float('-inf')] * m
            suff_min_minus = [float('inf')] * m
            suff_max_minus[m-1] = free_minus[m-1]
            suff_min_minus[m-1] = free_minus[m-1]
            for i in range(m-2, -1, -1):
                suff_max_minus[i] = max(suff_max_minus[i+1], free_minus[i])
                suff_min_minus[i] = min(suff_min_minus[i+1], free_minus[i])
            
            max_fixed = max(fixed) if fixed else float('-inf')
            min_fixed = min(fixed) if fixed else float('inf')
            
            best_range = float('inf')
            # p = number of free elements that receive +1 (prefix length)
            for p in range(m + 1):
                cur_max = max_fixed
                cur_min = min_fixed
                if p > 0:
                    cur_max = max(cur_max, pref_max_plus[p-1])
                    cur_min = min(cur_min, pref_min_plus[p-1])
                if p < m:
                    cur_max = max(cur_max, suff_max_minus[p])
                    cur_min = min(cur_min, suff_min_minus[p])
                best_range = min(best_range, cur_max - cur_min)
            return best_range
        
        answer_range = float('inf')
        for p in (0, 1):
            if mismatches[p] == k:
                answer_range = min(answer_range, min_range_for_pattern(p))
        
        return [k, int(answer_range)]
