"""
This module provides a solution to calculate the sum of all prime numbers
between an integer n and its digit-reversed counterpart.
"""

class Solution:  # pylint: disable=too-few-public-methods
    """
    A class used to encapsulate the prime sum logic.
    """

    def sumOfPrimesInRange(self, n):  # pylint: disable=invalid-name
        """
        Calculates the sum of primes between n and its reverse.

        :type n: int
        :rtype: int
        """
        # Reverse the digits of n by converting to string and slicing
        r = int(str(n)[::-1])

        # Define the range boundaries
        start = min(n, r)
        end = max(n, r)

        def is_prime(num):
            """Checks if a number is prime."""
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        # Sum all primes in the inclusive range [start, end]
        total_sum = 0
        for x in range(start, end + 1):
            if is_prime(x):
                total_sum += x

        return total_sum
