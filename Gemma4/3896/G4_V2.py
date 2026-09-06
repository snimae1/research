"""
Module to solve the alternating prime array problem.
This module calculates the minimum increments needed to make an array
alternating between prime and non-prime numbers.
"""

class Solution:
    """
    Provides a method to transform an integer array into an alternating prime array.
    """

    def min_operations(self, nums):
        """
        Calculates the minimum operations to ensure even indices are prime
        and odd indices are non-prime.

        :type nums: List[int]
        :rtype: int
        """
        # Limit is set slightly above 10^5 to account for increments
        # needed to reach the next prime number.
        limit = 110000
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        
        # Sieve of Eratosthenes to precompute prime numbers
        for p in range(2, int(limit**0.5) + 1):
            if is_prime[p]:
                for i in range(p * p, limit + 1, p):
                    is_prime[i] = False

        total_ops = 0
        
        for i, val in enumerate(nums):
            if i % 2 == 0:
                # Even index: Must be a prime number.
                # Increment until the closest prime is found.
                current = val
                while current <= limit and not is_prime[current]:
                    current += 1
                total_ops += (current - val)
            else:
                # Odd index: Must be a non-prime number.
                # Increment until the closest non-prime is found.
                current = val
                while current <= limit and is_prime[current]:
                    current += 1
                total_ops += (current - val)
                
        return total_ops
