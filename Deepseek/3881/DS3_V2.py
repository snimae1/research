"""Solution for counting visible people problem."""

# pylint: disable=invalid-name, too-few-public-methods

class Solution:
    """Provides a method to count possible direction assignments."""

    def countVisiblePeople(self, n, pos, k):
        """
        Return number of assignments where person at pos sees exactly k people.

        :type n: int
        :type pos: int
        :type k: int
        :rtype: int
        """
        _ = pos  # pos does not affect the number of visible others
        mod = 1_000_000_007

        total_others = n - 1
        visible_count = k

        if visible_count < 0 or visible_count > total_others:
            return 0

        # Precompute factorials modulo mod
        fact = [1] * (total_others + 1)
        for i in range(1, total_others + 1):
            fact[i] = (fact[i - 1] * i) % mod

        # Inverse factorials using Fermat's little theorem
        inv_fact = [1] * (total_others + 1)
        inv_fact[total_others] = pow(fact[total_others], mod - 2, mod)
        for i in range(total_others, 0, -1):
            inv_fact[i - 1] = (inv_fact[i] * i) % mod

        # Binomial coefficient C(n-1, k) modulo mod
        comb = fact[total_others] * inv_fact[visible_count] % mod
        comb = comb * inv_fact[total_others - visible_count] % mod

        return (2 * comb) % mod
