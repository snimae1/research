class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type s: str
        :type queries: List[str]
        :rtype: List[bool]
        """
        from collections import deque

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [0] * n
        heavy = [-1] * n

        # First DFS (iterative): parent/depth/order
        order = []
        stack = [0]
        parent[0] = 0
        while stack:
            u = stack.pop()
            order.append(u)
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.append(v)

        # Compute subtree sizes and heavy child
        for u in reversed(order):
            size[u] = 1
            best = 0
            for v in graph[u]:
                if v != parent[u]:
                    size[u] += size[v]
                    if size[v] > best:
                        best = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        cur = 0

        # Heavy-Light Decomposition
        stack = [(0, 0)]
        while stack:
            u, h = stack.pop()
            while u != -1:
                head[u] = h
                pos[u] = cur
                cur += 1

                light = []
                for v in graph[u]:
                    if v != parent[u] and v != heavy[u]:
                        light.append(v)
                for v in reversed(light):
                    stack.append((v, v))

                u = heavy[u]

        base = [0] * n
        chars = list(s)
        for i in range(n):
            base[pos[i]] = 1 << (ord(chars[i]) - ord('a'))

        # Segment Tree
        sizeST = 1
        while sizeST < n:
            sizeST <<= 1

        seg = [0] * (2 * sizeST)

        for i in range(n):
            seg[sizeST + i] = base[i]
        for i in range(sizeST - 1, 0, -1):
            seg[i] = seg[i << 1] ^ seg[i << 1 | 1]

        def update(idx, val):
            idx += sizeST
            seg[idx] = val
            idx >>= 1
            while idx:
                seg[idx] = seg[idx << 1] ^ seg[idx << 1 | 1]
                idx >>= 1

        def query_seg(l, r):
            res = 0
            l += sizeST
            r += sizeST
            while l <= r:
                if l & 1:
                    res ^= seg[l]
                    l += 1
                if not (r & 1):
                    res ^= seg[r]
                    r -= 1
                l >>= 1
                r >>= 1
            return res

        def query_path(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                res ^= query_seg(pos[head[u]], pos[u])
                u = parent[head[u]]
            if depth[u] > depth[v]:
                u, v = v, u
            res ^= query_seg(pos[u], pos[v])
            return res

        ans = []

        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                chars[u] = c
                update(pos[u], 1 << (ord(c) - ord('a')))
            else:
                u = int(parts[1])
                v = int(parts[2])
                mask = query_path(u, v)
                ans.append(mask == 0 or (mask & (mask - 1)) == 0)

        return ans
