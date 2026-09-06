"""
Module for solving the sum of primes in a range problem.
"""


class Solution:
    """
    Provides solution methods for coding challenges.
    """

    def sumOfPrimesInRange(self, n):
        """
        Calculate the sum of all prime numbers between n and its reverse.

        :type n: int
        :rtype: int
        """
        def is_prime(num):
            """Return True if num is a prime number, otherwise False."""
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        r = int(str(n)[::-1])
        start = min(n, r)
        end = max(n, r)

        prime_sum = 0
        for num in range(start, end + 1):
            if is_prime(num):
                prime_sum += num

        return prime_sum
