"""Solution for counting integers with valid adjacent digit differences."""

from functools import lru_cache

# The names of the class and method are required by the problem interface.

# pylint: disable=invalid-name,too-few-public-methods

class Solution(object):
"""Provide a solution for counting good integers in a given range."""

```
# Inheritance from object is required by the requested problem syntax.
# pylint: disable=useless-object-inheritance

def goodIntegers(self, l, r, k):
    """
    Return the number of good integers in the inclusive range [l, r].

    A number is good when the absolute difference between every pair
    of adjacent digits is at most k.

    The result is calculated using digit dynamic programming.
    """

    def count_good_numbers(limit):
        """
        Return the number of positive good integers less than or equal
        to limit.
        """
        if limit <= 0:
            return 0

        digits = [int(digit) for digit in str(limit)]
        length = len(digits)

        @lru_cache(maxsize=None)
        def digit_dp(position, previous_digit, started, tight):
            """
            Count valid numbers that can be formed from this state.

            position:
                Current digit position.

            previous_digit:
                The previous digit of the number currently being built.
                It is only relevant after the number has started.

            started:
                Indicates whether a non-leading-zero digit has appeared.

            tight:
                Indicates whether the current prefix is still equal to
                the prefix of the upper limit.
            """
            if position == length:
                return int(started)

            maximum_digit = digits[position] if tight else 9
            result = 0

            for current_digit in range(maximum_digit + 1):
                next_tight = (
                    tight and current_digit == maximum_digit
                )

                # Leading zeros are ignored because they are not part
                # of the actual representation of the number.
                if not started:
                    if current_digit == 0:
                        result += digit_dp(
                            position + 1,
                            -1,
                            False,
                            next_tight
                        )
                    else:
                        result += digit_dp(
                            position + 1,
                            current_digit,
                            True,
                            next_tight
                        )

                # Once the number has started, adjacent digits must
                # differ by at most k.
                elif abs(previous_digit - current_digit) <= k:
                    result += digit_dp(
                        position + 1,
                        current_digit,
                        True,
                        next_tight
                    )

            return result

        return digit_dp(0, -1, False, True)

    # Count numbers in [1, r] and subtract numbers in [1, l - 1].
    return count_good_numbers(r) - count_good_numbers(l - 1)
```
