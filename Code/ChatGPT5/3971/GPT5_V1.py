class Solution(object):
    def maxTotalValue(self, value, decay, m):
        """
        :type value: List[int]
        :type decay: List[int]
        :type m: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(value)

        def count_sum(x):
            cnt = 0
            total = 0
            equal = 0

            for v, d in zip(value, decay):
                if v < x:
                    continue

                k = (v - x) // d + 1
                cnt += k

                last = v - d * (k - 1)
                total += k * (v + last) // 2

                if last == x:
                    equal += 1

            return cnt, total, equal

        lo, hi = 1, max(value) + 1

        while lo < hi:
            mid = (lo + hi + 1) // 2
            cnt, _, _ = count_sum(mid)
            if cnt >= m:
                lo = mid
            else:
                hi = mid - 1

        T = lo
        cnt, total, equal = count_sum(T)

        # Zu viele Elemente mit Wert T entfernt
        total -= (cnt - m) * T

        return total % MOD
