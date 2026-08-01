class Solution(object):
    def evenSumSubgraphs(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        ans = 0
        # Iterate over all non-empty subsets (represented as bitmasks)
        for mask in range(1, 1 << n):
            # Check if sum of node values is even
            total = 0
            for i in range(n):
                if mask & (1 << i):
                    total += nums[i]
            if total % 2 != 0:
                continue
            
            # Check connectivity of the induced subgraph
            # Find the first node in the subset
            start = (mask & -mask).bit_length() - 1  # index of lowest set bit
            
            # BFS / DFS to traverse the subgraph
            visited = 0
            stack = [start]
            visited |= (1 << start)
            
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if (mask & (1 << v)) and not (visited & (1 << v)):
                        visited |= (1 << v)
                        stack.append(v)
            
            # If all nodes in the subset were visited, it is connected
            if visited == mask:
                ans += 1
                
        return ans
