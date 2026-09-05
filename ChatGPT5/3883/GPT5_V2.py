```python
"""Solution for counting non-decreasing arrays with given digit sums."""

MOD = 10**9 + 7
MAX_VALUE = 5000


class Solution:
    """Solve the digit-sum array counting problem."""

    def countArrays(self, digitSum):
        """
        Count valid non-decreasing arrays.

        :param digitSum: Required digit sum for every array position.
        :return: Number of valid arrays modulo 10**9 + 7.
        """
        numbers = self._group_numbers_by_digit_sum()

        # A digit sum above 40 is impossible for numbers <= 5000.
        if any(value > 40 or not numbers[value] for value in digitSum):
            return 0

        # dp[i] = number of valid arrays ending with numbers[i].
        previous = numbers[digitSum[0]]
        dp = [1] * len(previous)

        for value in digitSum[1:]:
            current = numbers[value]
            dp = self._next_dp(previous, dp, current)
            previous = current

        return sum(dp) % MOD

    @staticmethod
    def _digit_sum(number):
        """Return the sum of the decimal digits of number."""
        return sum(map(int, str(number)))

    def _group_numbers_by_digit_sum(self):
        """Group all numbers from 0 to 5000 by their digit sum."""
        groups = [[] for _ in range(41)]

        for number in range(MAX_VALUE + 1):
            groups[self._digit_sum(number)].append(number)

        return groups

    @staticmethod
    def _next_dp(previous, dp, current):
        """
        Calculate DP values for the next digit-sum group.

        For every current value, all previous values <= current are valid.
        Prefix sums allow this to be calculated in linear time.
        """
        prefix = [0]

        for count in dp:
            prefix.append((prefix[-1] + count) % MOD)

        result = []
        previous_index = 0

        for number in current:
            while (
                previous_index < len(previous)
                and previous[previous_index] <= number
            ):
                previous_index += 1

            result.append(prefix[previous_index])

        return result
```
