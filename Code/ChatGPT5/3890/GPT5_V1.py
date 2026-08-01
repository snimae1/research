class Solution(object):
    def findGoodIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        from math import isqrt

        # Größter möglicher Wert für a bzw. b
        limit = int(round(n ** (1.0 / 3)))
        while (limit + 1) ** 3 <= n:
            limit += 1
        while limit ** 3 > n:
            limit -= 1

        sums = {}

        # Alle möglichen Paare (a, b) mit a <= b erzeugen
        for a in range(1, limit + 1):
            a3 = a * a * a
            for b in range(a, limit + 1):
                s = a3 + b * b * b
                if s > n:
                    break
                if s not in sums:
                    sums[s] = 1
                else:
                    sums[s] += 1

        ans = []
        for value in sorted(sums):
            if sums[value] >= 2:
                ans.append(value)

        return ans
