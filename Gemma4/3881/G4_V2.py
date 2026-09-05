"""
This module provides a solution to calculate the number of ways people in a line
can be assigned directions ('L' or 'R') such that a person at a given position
sees exactly k people.
"""

class Solution:
    """
    A class containing the logic to solve the visible people counting problem.
    """

    # pylint: disable=too-few-public-methods
    def countVisiblePeople(self, n, pos, k):
        """
        Calculates the number of possible direction assignments such that
        the person at index 'pos' sees exactly k people.

        :type n: int - Total number of people
        :type pos: int - Position of the observer
        :type k: int - Number of people the observer must see
        :rtype: int - Number of ways modulo 10^9 + 7
        """
        # The observer's position 'pos' does not affect the total number of people
        # they could potentially see (which is always n-1), but it is part of the input.
        # To satisfy Pylint's unused-argument check:
        _ = pos
        
        mod_val = 10**9 + 7
        
        # If k is greater than the number of other people, it is impossible.
        if k > n - 1:
            return 0
        
        def calculate_combinations(n_val, r_val, p_val):
            """
            Computes the binomial coefficient C(n, r) modulo p.
            """
            if r_val < 0 or r_val > n_val:
                return 0
            if r_val in (0, n_val):
                return 1
            if r_val > n_val // 2:
                r_val = n_val - r_val
                
            numerator = 1
            denominator = 1
            for i in range(r_val):
                numerator = (numerator * (n_val - i)) % p_val
                denominator = (denominator * (i + 1)) % p_val
            
            # Modular inverse using Fermat's Little Theorem
            return (numerator * pow(denominator, p_val - 2, p_val)) % p_val

        # We need to choose k people to be visible out of n-1 candidates.
        # Every person has exactly 1 way to be visible and 1 way to be invisible.
        # The observer at 'pos' can choose 'L' or 'R' (2 options), which doesn't
        # affect who they see.
        combinations = calculate_combinations(n - 1, k, mod_val)
        
        return (combinations * 2) % mod_val
