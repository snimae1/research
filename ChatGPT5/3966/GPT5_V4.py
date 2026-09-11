"""Solution for counting integers with valid adjacent digit differences."""

from functools import lru_cache


# The names of the class and method are required by the problem interface.
# pylint: disable=invalid-name,too-few-public-methods


class Solution(object):
    """Provide a solution for counting good integers."""

    # Required by the requested problem syntax.
    # pylint: disable=useless-object-inheritance

    def goodIntegers(self, l, r, k):
        """
        Return the number of good integers in the range [l, r].

        A number is good if the absolute difference between
        every pair of adjacent digits is at most k.
        """

        def count_good_numbers(limit):
            """Count good positive integers less than or equal to limit."""
            if limit <= 0:
                return 0

            digits = [int(digit) for digit in str(limit)]
            length = len(digits)

            @lru_cache(maxsize=None)
            def digit_dp(position, previous_digit, started, tight):
                """
                Count valid numbers from the current DP state.

                position:
                    Current position in the number.

                previous_digit:
                    Previous digit of the number.
                    -1 means that the number has not started yet.

                started:
                    True if a non-leading-zero digit has been chosen.

                tight:
                    True if the current prefix is equal to the limit's prefix.
                """
                if position == length:
                    return int(started)

                maximum_digit = digits[position] if tight else 9
                result = 0

                for current_digit in range(maximum_digit + 1):
                    next_tight = (
                        tight and current_digit == maximum_digit
                    )

                    # Ignore leading zeros because they are not
                    # part of the actual number.
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

                    # Check the difference between adjacent digits.
                    elif abs(previous_digit - current_digit) <= k:
                        result += digit_dp(
                            position + 1,
                            current_digit,
                            True,
                            next_tight
                        )

                return result

            return digit_dp(0, -1, False, True)

        # Count good numbers up to r and subtract those below l.
        return count_good_numbers(r) - count_good_numbers(l - 1)
