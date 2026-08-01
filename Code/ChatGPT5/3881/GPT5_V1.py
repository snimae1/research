class Solution(object):
    def countVisiblePeople(self, n, pos, k):
        """
        :type n: int
        :type pos: int
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        left = pos
        right = n - pos - 1

        # Fakultäten und inverse Fakultäten
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        invfact = [1] * (n + 1)
        invfact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            invfact[i - 1] = invfact[i] * i % MOD

        def C(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * invfact[b] % MOD * invfact[a - b] % MOD

        ans = 0

        lo = max(0, k - right)
        hi = min(left, k)

        for x in range(lo, hi + 1):
            ans = (ans + C(left, x) * C(right, k - x)) % MOD

        # Die Person an pos kann beliebig L oder R wählen.
        return (ans * 2) % MOD
