"""Find the minimum operations needed to create k peaks in a circular array."""


class Solution:
    """Solve the circular peak optimization problem."""

    def minOperations(self, nums, k):
        """
        Return the minimum number of increments needed to create k peaks.

        A peak must be strictly greater than both of its neighbors.
        """
        n = len(nums)

        if k == 0:
            return 0

        # Two peaks can never be adjacent in a circular array.
        if k > n // 2:
            return -1

        # Try both possibilities for index 0:
        # it is either a peak or it is not.
        answer = min(
            self._solve_case(nums, k, first_is_peak=False),
            self._solve_case(nums, k, first_is_peak=True)
        )

        return answer

    def _solve_case(self, nums, k, first_is_peak):
        """Calculate the minimum cost for one choice of index 0."""
        n = len(nums)
        infinity = float("inf")

        # dp[peak_count][previous_peak]:
        # minimum cost after processing the current part of the array.
        dp = [[infinity] * 2 for _ in range(k + 1)]

        if first_is_peak:
            first_cost = self._peak_cost(nums, 0)
            dp[1][1] = first_cost
        else:
            dp[0][0] = 0

        for index in range(1, n):
            next_dp = [[infinity] * 2 for _ in range(k + 1)]

            for peak_count in range(k + 1):
                for previous_peak in range(2):
                    current_cost = dp[peak_count][previous_peak]

                    if current_cost == infinity:
                        continue

                    # Option 1: index is not a peak.
                    if current_cost < next_dp[peak_count][0]:
                        next_dp[peak_count][0] = current_cost

                    # Option 2: index becomes a peak.
                    if peak_count == k or previous_peak:
                        continue

                    # Index 0 and index n - 1 are neighbors.
                    if index == n - 1 and first_is_peak:
                        continue

                    cost = self._peak_cost(nums, index)
                    new_cost = current_cost + cost

                    if new_cost < next_dp[peak_count + 1][1]:
                        next_dp[peak_count + 1][1] = new_cost

            dp = next_dp

        return min(dp[k])

    @staticmethod
    def _peak_cost(nums, index):
        """Return the increments required to make index a peak."""
        n = len(nums)

        left = nums[(index - 1) % n]
        right = nums[(index + 1) % n]
        required_value = max(left, right) + 1

        return max(0, required_value - nums[index])
