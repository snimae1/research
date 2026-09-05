"""
This module provides a solution to count the number of non-decreasing arrays
where each element's sum of digits matches a given sequence of digit sums.
"""

class Solution:
    """
    A class containing the logic to solve the digit sum array problem.
    """

    def countArrays(self, digitSum): # pylint: disable=invalid-name
        """
        Counts distinct non-decreasing arrays where each element is in [0, 5000]
        and its sum of digits equals the corresponding value in digitSum.

        :type digitSum: List[int] # pylint: disable=invalid-name
        :rtype: int
        """
        # Constants for calculation
        mod_val = 10**9 + 7
        max_limit = 5000

        # Precompute the sum of digits for all numbers from 0 to 5000.
        # This avoids repetitive calculations inside the DP loop.
        digit_sums_lookup = [0] * (max_limit + 1)
        for i in range(max_limit + 1):
            s = 0
            temp = i
            while temp > 0:
                s += temp % 10
                temp //= 10
            digit_sums_lookup[i] = s

        n = len(digitSum) # pylint: disable=invalid-name
        # dp[v] stores the number of valid arrays ending with the value v.
        dp = [0] * (max_limit + 1)

        # Initialization: Handle the first required digit sum.
        first_target = digitSum[0] # pylint: disable=invalid-name
        for v in range(max_limit + 1):
            if digit_sums_lookup[v] == first_target:
                dp[v] = 1

        # Process each subsequent required digit sum in the input array.
        for i in range(1, n):
            current_target = digitSum[i] # pylint: disable=invalid-name

            # Use a prefix sum array to optimize the transition.
            # prefix_sum[v+1] = sum of dp[0...v].
            # This reduces complexity from O(N * MAX_VAL^2) to O(N * MAX_VAL).
            prefix_sum = [0] * (max_limit + 2)
            for v in range(max_limit + 1):
                prefix_sum[v + 1] = (prefix_sum[v] + dp[v]) % mod_val

            new_dp = [0] * (max_limit + 1)
            # A number v is a candidate if its digit sum matches the current target.
            for v in range(max_limit + 1):
                if digit_sums_lookup[v] == current_target:
                    # The array remains non-decreasing if the previous element <= v.
                    new_dp[v] = prefix_sum[v + 1]

            dp = new_dp

        # The answer is the sum of all possibilities for the final element.
        return sum(dp) % mod_val
