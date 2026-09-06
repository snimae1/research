"""
Solution for counting "good integers" in a range [l, r] where the absolute
difference between every pair of adjacent digits is at most k.
"""

from functools import lru_cache


# pylint: disable=too-few-public-methods, invalid-name
class Solution:
    """
    Provides a method to count good integers in a given inclusive range.
    """

    def goodIntegers(self, l: int, r: int, k: int) -> int:
        """
        Returns the number of integers in [l, r] that are considered good.

        A number is good if the absolute difference between every pair of
        adjacent digits is at most k.

        :param l: Lower bound of the range (inclusive), l >= 10.
        :param r: Upper bound of the range (inclusive), r <= 10^15.
        :param k: Maximum allowed absolute difference between adjacent digits.
        :return: Count of good integers in the range.
        """
        def count_up_to(n: int) -> int:
            """Count good numbers from 0 to n (inclusive)."""
            if n < 0:
                return 0
            s = str(n)

            @lru_cache(maxsize=None)
            def dp(i: int, prev: int, tight: bool, started: bool) -> int:
                """
                Digit DP recursive function.

                :param i: Current index in the string representation of n.
                :param prev: Previous digit (10 means no previous digit yet,
                             i.e., we are still in leading zeros).
                :param tight: True if the prefix formed so far equals n's prefix.
                :param started: True if at least one non-zero digit has been placed.
                :return: Number of valid completions from this state.
                """
                # Base case: all digits have been processed.
                if i == len(s):
                    # A number is valid if it has at least one digit (started=True).
                    # The number 0 is represented by started=False, but since l >= 10,
                    # including 0 in the count does not affect the final answer.
                    return 1 if started else 0

                # Determine the maximum digit we can place at this position.
                limit = int(s[i]) if tight else 9
                total = 0

                # Try all possible digits for this position.
                for d in range(limit + 1):
                    next_tight = tight and (d == limit)
                    next_started = started or (d != 0)

                    if not next_started:
                        # Still in leading zeros: no previous digit constraint applies.
                        total += dp(i + 1, 10, next_tight, False)
                    else:
                        if not started:
                            # Placing the first non-zero digit: no adjacency check needed.
                            total += dp(i + 1, d, next_tight, True)
                        else:
                            # Check the absolute difference with the previous digit.
                            if abs(d - prev) <= k:
                                total += dp(i + 1, d, next_tight, True)

                return total

            # Start from the most significant digit with no previous digit,
            # tight bound active, and no non-zero digit placed yet.
            return dp(0, 10, True, False)

        # Count good integers in [0, r] and subtract those in [0, l-1].
        return count_up_to(r) - count_up_to(l - 1)


# Optional quick test
if __name__ == "__main__":
    sol = Solution()
    print(sol.goodIntegers(10, 15, 1))    # Expected: 3
    print(sol.goodIntegers(201, 204, 2))  # Expected: 2
