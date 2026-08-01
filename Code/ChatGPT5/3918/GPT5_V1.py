class Solution(object):
    def sumOfPrimesInRange(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Zahl umdrehen
        r = int(str(n)[::-1])

        left = min(n, r)
        right = max(n, r)

        def isPrime(x):
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False

            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

        total = 0
        for num in range(left, right + 1):
            if isPrime(num):
                total += num

        return total
