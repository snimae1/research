from math import gcd

class Solution(object):
    def countGoodSubseq(self, nums, p, queries):
        """
        :type nums: List[int]
        :type p: int
        :type queries: List[List[int]]
        :rtype: int
        """

        n = len(nums)

        size = 1
        while size < n:
            size <<= 1

        INF = 0

        tree = [0] * (2 * size)
        divCnt = 0

        arr = [0] * n

        for i, x in enumerate(nums):
            if x % p == 0:
                arr[i] = x // p
                divCnt += 1
            else:
                arr[i] = 0

        for i in range(n):
            tree[size + i] = arr[i]
        for i in range(size - 1, 0, -1):
            tree[i] = gcd(tree[i << 1], tree[i << 1 | 1])

        def update(idx, val):
            pos = size + idx
            tree[pos] = val
            pos >>= 1
            while pos:
                tree[pos] = gcd(tree[pos << 1], tree[pos << 1 | 1])
                pos >>= 1

        ans = 0

        for idx, val in queries:

            old = nums[idx]

            if old % p == 0:
                divCnt -= 1
            nums[idx] = val
            if val % p == 0:
                divCnt += 1

            if val % p == 0:
                arr[idx] = val // p
            else:
                arr[idx] = 0

            update(idx, arr[idx])

            if divCnt == 0:
                continue

            totalG = tree[1]

            if totalG != 1:
                continue

            # Falls mindestens ein Element nicht durch p teilbar ist,
            # kann man dieses einfach weglassen.
            if divCnt < n:
                ans += 1
                continue

            # Alle Elemente sind durch p teilbar.
            # Prüfen, ob nach Entfernen eines Elements
            # der GCD weiterhin 1 bleibt.

            pref = [0] * (n + 1)
            suf = [0] * (n + 1)

            for i in range(n):
                pref[i + 1] = gcd(pref[i], arr[i])

            for i in range(n - 1, -1, -1):
                suf[i] = gcd(suf[i + 1], arr[i])

            ok = False
            for i in range(n):
                if gcd(pref[i], suf[i + 1]) == 1:
                    ok = True
                    break

            if ok:
                ans += 1

        return ans
