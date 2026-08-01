class Solution(object):
    def evenSumSubgraphs(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(nums)

        # Store graph as bitmasks
        adj = [0] * n
        for u, v in edges:
            adj[u] |= (1 << v)
            adj[v] |= (1 << u)

        ans = 0

        # Enumerate all non-empty subsets
        for mask in range(1, 1 << n):
            # Check if sum of values is even
            parity = 0
            temp = mask
            while temp:
                bit = temp & -temp
                node = bit.bit_length() - 1
                parity ^= nums[node]
                temp -= bit

            if parity != 0:
                continue

            # Check connectivity of induced subgraph
            start = mask & -mask
            seen = start
            stack = start

            while stack:
                bit = stack & -stack
                stack -= bit
                node = bit.bit_length() - 1

                neighbors = adj[node] & mask & ~seen
                seen |= neighbors
                stack |= neighbors

            if seen == mask:
                ans += 1

        return ans
