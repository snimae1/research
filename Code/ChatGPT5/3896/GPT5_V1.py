class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_val = max(nums)

        # Obergrenze für die nächste Primzahl.
        # Für Zahlen <= 1e5 reichen +300 sicher aus.
        limit = max_val + 300

        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False

        p = 2
        while p * p <= limit:
            if is_prime[p]:
                for multiple in range(p * p, limit + 1, p):
                    is_prime[multiple] = False
            p += 1

        # next_prime[x] = kleinste Primzahl >= x
        next_prime = [0] * (limit + 2)
        nxt = -1
        for i in range(limit, -1, -1):
            if is_prime[i]:
                nxt = i
            next_prime[i] = nxt

        ans = 0

        for i, x in enumerate(nums):
            if i % 2 == 0:
                # Muss prim sein
                ans += next_prime[x] - x
            else:
                # Muss nicht prim sein
                if is_prime[x]:
                    y = x
                    while is_prime[y]:
                        y += 1
                    ans += y - x

        return ans
