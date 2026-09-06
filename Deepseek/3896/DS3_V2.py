"""
Solution for the "Minimum Operations to Make Array Alternating Prime" problem.

This module provides a class with a method to compute the minimum number of
increment operations needed to transform an integer array into an alternating
prime array (primes at even indices, non-primes at odd indices).
"""


class Solution:
    """Contains the method to solve the alternating prime transformation problem."""

    # pylint: disable=too-few-public-methods
    def minOperations(self, nums):
        # pylint: disable=invalid-name
        """
        Return the minimum number of operations to make nums alternating prime.

        An operation increments any element by 1. Even indices must become prime,
        odd indices must become non-prime.

        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # Determine a safe upper bound for the sieve.
        # The largest number we may ever need is slightly above the current maximum,
        # because prime gaps are small in this range.
        max_val = max(nums) + 200
        max_val = max(max_val, 2)  # ensure at least 2 for the sieve

        # Sieve of Eratosthenes to precompute prime numbers up to max_val.
        is_prime = [True] * (max_val + 1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(max_val ** 0.5) + 1):
            if is_prime[p]:
                for multiple in range(p * p, max_val + 1, p):
                    is_prime[multiple] = False

        total_ops = 0
        for index, value in enumerate(nums):
            if index % 2 == 0:
                # Even index: must become a prime number.
                if not is_prime[value]:
                    # Find the next prime greater than or equal to value.
                    candidate = value
                    while candidate <= max_val and not is_prime[candidate]:
                        candidate += 1
                    total_ops += candidate - value
            else:
                # Odd index: must become a non-prime number.
                if is_prime[value]:
                    if value == 2:
                        total_ops += 2  # 2 -> 4 (first non-prime after 2)
                    else:
                        total_ops += 1  # any other prime -> next integer (even > 2, hence composite)
        return total_ops
