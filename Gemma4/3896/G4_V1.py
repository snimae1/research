class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Da die Constraints bis 10^5 gehen und wir Zahlen inkrementieren,
        # erstellen wir ein Sieb bis etwas über 100.000, um den nächsten Primzahl-Kandidaten zu finden.
        LIMIT = 110000 
        is_prime = [True] * (LIMIT + 1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(LIMIT**0.5) + 1):
            if is_prime[p]:
                for i in range(p * p, LIMIT + 1, p):
                    is_prime[i] = False

        total_ops = 0
        
        for i in range(len(nums)):
            val = nums[i]
            if i % 2 == 0:
                # Index ist gerade -> Muss eine PRIMZAHL sein
                current = val
                while current <= LIMIT and not is_prime[current]:
                    current += 1
                total_ops += (current - val)
            else:
                # Index ist ungerade -> Muss KEINE Primzahl sein
                current = val
                while current <= LIMIT and is_prime[current]:
                    current += 1
                total_ops += (current - val)
                
        return total_ops
