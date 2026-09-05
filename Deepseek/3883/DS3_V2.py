"""
Solution for counting valid non-decreasing arrays based on digit sums.
"""

class Solution(object):  # pylint: disable=useless-object-inheritance
    """
    Provides a method to count valid arrays where each element's digit sum
    matches the given target and the array is non-decreasing.
    """

    # pylint: disable=invalid-name
    def countArrays(self, digitSum):
        """
        Counts the number of valid non-decreasing arrays of length n.

        Each element arr[i] must satisfy 0 <= arr[i] <= 5000,
        its digit sum must equal digitSum[i], and the array must be non-decreasing.

        :type digitSum: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        max_val = 5000

        # Precompute all numbers in [0, 5000] grouped by their digit sum.
        # Maximum possible digit sum for numbers <= 5000 is 31, but we allow up to 50.
        digit_to_vals = [[] for _ in range(51)]
        for value in range(max_val + 1):
            digit_sum = sum(int(d) for d in str(value))
            if digit_sum <= 50:
                digit_to_vals[digit_sum].append(value)

        # If any required digit sum has no valid numbers, answer is 0.
        for required_sum in digitSum:
            if not digit_to_vals[required_sum]:
                return 0

        n = len(digitSum)

        # dp[value] = number of valid non-decreasing arrays ending with 'value'.
        dp = [0] * (max_val + 1)
        for value in digit_to_vals[digitSum[0]]:
            dp[value] = 1

        # Process remaining positions.
        for i in range(1, n):
            target_sum = digitSum[i]
            candidates = digit_to_vals[target_sum]  # already sorted

            # Build prefix sums over dp for quick range queries.
            pref = [0] * (max_val + 1)
            acc = 0
            for value in range(max_val + 1):
                acc = (acc + dp[value]) % mod
                pref[value] = acc

            new_dp = [0] * (max_val + 1)
            for value in candidates:
                # Any previous value u <= value is allowed.
                new_dp[value] = pref[value]
            dp = new_dp

        return sum(dp) % mod
