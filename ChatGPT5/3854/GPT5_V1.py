class Solution(object):
    def makeParityAlternating(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 1:
            return [0, 0]

        INF = 10 ** 30

        def solve(start_parity):
            # cost = minimale Anzahl Operationen
            cost = 0

            # Intervalle der möglichen Werte nach genau minimalen Operationen
            low = []
            high = []

            for i, x in enumerate(nums):
                want = (start_parity + i) & 1

                if (x & 1) == want:
                    cost_i = 0
                    l = r = x
                else:
                    cost_i = 1
                    l = x - 1
                    r = x + 1

                cost += cost_i
                low.append(l)
                high.append(r)

            # Binäre Suche auf minimale Spannweite
            lo = 0
            hi = max(high) - min(low)

            def feasible(D):
                L = -INF
                R = INF
                for l, r in zip(low, high):
                    L = max(L, l - D)
                    R = min(R, r)
                    if L > R:
                        return False
                return True

            while lo < hi:
                mid = (lo + hi) // 2
                if feasible(mid):
                    hi = mid
                else:
                    lo = mid + 1

            return cost, lo

        c0, d0 = solve(0)   # gerade, ungerade, ...
        c1, d1 = solve(1)   # ungerade, gerade, ...

        if c0 < c1:
            return [c0, d0]
        if c1 < c0:
            return [c1, d1]
        return [c0, min(d0, d1)]
