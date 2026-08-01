class Solution(object):
    def maxAlternatingSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        class Fenwick:
            def __init__(self, n):
                self.n = n
                self.bit = [-10**18] * (n + 1)

            def update(self, i, val):
                while i <= self.n:
                    if val > self.bit[i]:
                        self.bit[i] = val
                    i += i & -i

            def query(self, i):
                res = -10**18
                while i > 0:
                    if self.bit[i] > res:
                        res = self.bit[i]
                    i -= i & -i
                return res

        n = len(nums)

        # Coordinate compression
        vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)

        # down: last comparison was nums[prev] > nums[current]
        # up:   last comparison was nums[prev] < nums[current]
        up = [0] * n
        down = [0] * n

        # Fenwick for querying:
        # max down[j] where nums[j] < x
        bit_down = Fenwick(m)

        # max up[j] where nums[j] > x (using reversed ranks)
        bit_up = Fenwick(m)

        ans = 0

        for i in range(n):
            # Add indices that are far enough away to be predecessors
            j = i - k
            if j >= 0:
                rj = rank[nums[j]]
                bit_down.update(rj, down[j])
                bit_up.update(m - rj + 1, up[j])

            r = rank[nums[i]]

            # Start with a subsequence of length 1
            up[i] = nums[i]
            down[i] = nums[i]

            # Previous value < current value -> sequence ends with an "up"
            best = bit_down.query(r - 1)
            if best > -10**17:
                up[i] = max(up[i], best + nums[i])

            # Previous value > current value -> sequence ends with a "down"
            # Values greater than nums[i] correspond to reversed ranks < m-r+1
            best = bit_up.query(m - r)
            if best > -10**17:
                down[i] = max(down[i], best + nums[i])

            ans = max(ans, up[i], down[i])

        return ans
