"""Determine whether a permutation of a number is digitorial."""


class Solution:
    """Provide a solution for the digitorial permutation problem."""

    def isDigitorialPermutation(self, n):
        """Return True if a permutation of n is a digitorial number.

        The sum of the factorials of the digits is independent of their
        order. Therefore, we only need to check whether this sum consists
        of exactly the same digits as n.
        """
        # Factorials for the digits 0 through 9.
        factorials = (
            1,      # 0!
            1,      # 1!
            2,      # 2!
            6,      # 3!
            24,     # 4!
            120,    # 5!
            720,    # 6!
            5040,   # 7!
            40320,  # 8!
            362880  # 9!
        )

        # Calculate the sum of the factorials of all digits in n.
        factorial_sum = sum(
            factorials[int(digit)]
            for digit in str(n)
        )

        # A valid permutation must contain exactly the same digits.
        return sorted(str(n)) == sorted(str(factorial_sum))
