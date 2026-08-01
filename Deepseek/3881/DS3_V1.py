
class Solution(object):
    def countVisiblePeople(self, n, pos, k):
        """
        :type n: int
        :type pos: int
        :type k: int
        :rtype: int
        """
        MOD = 1_000_000_007
        
        # Total people besides the observer = n - 1
        # If k is out of possible range, 0 ways.
        if k < 0 or k > n - 1:
            return 0
        
        N = n - 1
        K = k
        
        # Precompute factorials up to N modulo MOD
        fact = [1] * (N + 1)
        for i in range(1, N + 1):
            fact[i] = (fact[i - 1] * i) % MOD
            
        # Inverse factorials using Fermat's little theorem
        inv_fact = [1] * (N + 1)
        inv_fact[N] = pow(fact[N], MOD - 2, MOD)
        for i in range(N, 0, -1):
            inv_fact[i - 1] = (inv_fact[i] * i) % MOD
            
        # Binomial coefficient C(n-1, k) modulo MOD
        comb = fact[N] * inv_fact[K] % MOD * inv_fact[N - K] % MOD
        
        # The observer has 2 independent choices (L or R)
        ans = (2 * comb) % MOD
        return ans
