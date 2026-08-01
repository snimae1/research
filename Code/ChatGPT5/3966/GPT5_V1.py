from functools import lru_cache

class Solution(object):
    def goodIntegers(self, l, r, k):
        """
        :type l: int
        :type r: int
        :type k: int
        :rtype: int
        """

        def count(limit):
            if limit < 0:
                return 0

            digits = list(map(int, str(limit)))
            n = len(digits)

            @lru_cache(None)
            def dfs(pos, prev, started, tight):
                if pos == n:
                    return 1 if started else 0

                up = digits[pos] if tight else 9
                ans = 0

                for d in range(up + 1):
                    ntight = tight and (d == up)

                    if not started:
                        if d == 0:
                            ans += dfs(pos + 1, 10, False, ntight)
                        else:
                            ans += dfs(pos + 1, d, True, ntight)
                    else:
                        if abs(prev - d) <= k:
                            ans += dfs(pos + 1, d, True, ntight)

                return ans

            return dfs(0, 10, False, True)

        return count(r) - count(l - 1)
