class Solution(object):
    def findGoodIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        count = {}
        # Da a^3 + b^3 <= n <= 10^9, sind a und b maximal 1000.
        # Wir berechnen ein sicheres Maximum für a.
        max_a = int(n ** (1/3)) + 2  # +2 um Rundungsfehler zu vermeiden
        
        for a in range(1, max_a + 1):
            a3 = a * a * a
            if a3 > n:
                break
            # b läuft von a bis zum maximal möglichen Wert
            max_b = int((n - a3) ** (1/3)) + 1
            for b in range(a, max_b + 1):
                b3 = b * b * b
                sum_cubes = a3 + b3
                if sum_cubes > n:
                    break
                count[sum_cubes] = count.get(sum_cubes, 0) + 1

        # Alle Summen mit mindestens zwei verschiedenen Paaren (a, b)
        result = [num for num, cnt in count.items() if cnt >= 2]
        result.sort()
        return result
