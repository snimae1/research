"""
Module for solving the problem of counting connected even-sum subgraphs.
"""

class Solution:
    """
    Provides a method to count connected subgraphs with even sum of node values.
    """
    def evenSumSubgraphs(self, nums, edges):
        """
        Counts the number of non-empty subsets of nodes that induce a connected subgraph
        and have an even sum of node values.

        Args:
            nums (List[int]): List of 0/1 values for each node.
            edges (List[List[int]]): List of edges as [u, v].

        Returns:
            int: The number of valid subsets.
        """
        n = len(nums)
        # Build adjacency list for the graph
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ans = 0
        # Iterate over all non-empty subsets represented as bitmasks
        for mask in range(1, 1 << n):
            # Check if sum of node values in this subset is even
            total = 0
            for i in range(n):
                if mask & (1 << i):
                    total += nums[i]
            if total % 2 != 0:
                continue

            # Check connectivity using DFS from the first node in the subset
            start = (mask & -mask).bit_length() - 1  # index of lowest set bit
            visited = 0
            stack = [start]
            visited |= (1 << start)

            while stack:
                u = stack.pop()
                for v in adj[u]:
                    in_subset = mask & (1 << v)
                    is_visited = visited & (1 << v)
                    if in_subset and not is_visited:
                        visited |= (1 << v)
                        stack.append(v)

            # If all nodes in the subset were visited, it is connected
            if visited == mask:
                ans += 1

        return ans
