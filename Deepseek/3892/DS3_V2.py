"""
Solution for the "Minimum Operations to Make at Least K Peaks" problem.
"""


class Solution(object):
    # pylint: disable=too-few-public-methods, useless-object-inheritance, invalid-name
    def minOperations(self, nums, k):
        """
        Returns the minimum number of operations to obtain at least k peaks
        in the circular array nums. A peak is an element strictly greater
        than both its circular neighbours.

        The problem is equivalent to selecting a set of non-adjacent indices
        (in circular sense) with minimum total cost, where the cost of making
        index i a peak independently is c[i].

        Because the array is circular, index 0 and n-1 cannot both be peaks.
        We therefore split the problem into two cases:
          1. Index 0 is not chosen -> consider the linear array c[1:] (indices 1..n-1)
          2. Index 0 is chosen      -> consider c[0] plus c[2:n-1] (indices 2..n-2)
        In both cases the remaining problem is a classic "maximum weight independent set
        on a path" with a required number of elements, solved by dynamic programming.
        """
        n = len(nums)
        if k == 0:
            return 0
        # Maximum possible number of peaks in a circular array is floor(n/2)
        if k > n // 2:
            return -1

        # Cost to make each index i a peak independently (only increase nums[i]).
        cost = [0] * n
        for i in range(n):
            left = nums[i - 1] if i > 0 else nums[-1]
            right = nums[i + 1] if i < n - 1 else nums[0]
            required = max(left, right) + 1
            if required > nums[i]:
                cost[i] = required - nums[i]
            else:
                cost[i] = 0

        inf = 10**15  # A large value representing "impossible"

        def min_cost_linear(costs, need):
            """
            Given a list of costs for positions in a linear array,
            return the minimum total cost to select exactly `need`
            positions, no two of which are adjacent.
            Returns inf if impossible.
            """
            m = len(costs)
            if need == 0:
                return 0
            max_possible = (m + 1) // 2
            if need > max_possible:
                return inf

            # dp0[j] = min cost for j selections, last element NOT taken
            # dp1[j] = min cost for j selections, last element taken
            dp0 = [inf] * (need + 1)
            dp1 = [inf] * (need + 1)
            dp0[0] = 0
            if need >= 1:
                dp1[1] = costs[0]

            for i in range(1, m):
                cst = costs[i]
                limit = min(need, (i + 2) // 2)
                new_dp0 = [inf] * (need + 1)
                new_dp1 = [inf] * (need + 1)
                for j in range(limit + 1):
                    # Skip current element
                    new_dp0[j] = min(dp0[j], dp1[j])
                    # Take current element (only possible if we didn't take previous)
                    if j > 0 and dp0[j - 1] < inf:
                        new_dp1[j] = dp0[j - 1] + cst
                dp0, dp1 = new_dp0, new_dp1

            return min(dp0[need], dp1[need])

        # Case 1: index 0 is not a peak -> we only look at indices 1..n-1
        ans1 = min_cost_linear(cost[1:], k)

        # Case 2: index 0 is a peak -> we need k-1 more peaks from indices 2..n-2
        if k == 1:
            ans2 = cost[0]
        else:
            sub_costs = cost[2:n - 1] if n > 2 else []
            if not sub_costs:
                ans2 = inf
            else:
                ans2 = cost[0] + min_cost_linear(sub_costs, k - 1)

        answer = min(ans1, ans2)
        return answer if answer < inf else -1
