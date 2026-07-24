class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        # ---------- build adjacency ----------
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # bitmask for each node
        val_mask = [1 << (ord(ch) - 97) for ch in s]

        LOG = (n).bit_length()          # enough for 2^LOG > n
        up = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        pref = [0] * n                  # xor from root to node (inclusive)
        euler = [0] * n                 # node at each tin

        # ---------- iterative DFS to get parent, depth, tin, tout, pref ----------
        timer = 0
        stack = [(0, -1, 0)]            # (node, parent, state) 0=enter, 1=exit
        while stack:
            node, par, state = stack.pop()
            if state == 0:
                tin[node] = timer
                euler[timer] = node
                timer += 1

                up[0][node] = par if par != -1 else node
                if par == -1:
                    depth[node] = 0
                    pref[node] = val_mask[node]
                else:
                    depth[node] = depth[par] + 1
                    pref[node] = pref[par] ^ val_mask[node]

                stack.append((node, par, 1))
                # push children (reverse order not important)
                for nei in reversed(adj[node]):
                    if nei != par:
                        stack.append((nei, node, 0))
            else:
                tout[node] = timer - 1   # inclusive

        # ---------- binary lifting ----------
        for k in range(1, LOG):
            prev = up[k - 1]
            cur = up[k]
            for v in range(n):
                cur[v] = prev[prev[v]]

        # ---------- Fenwick tree (XOR) for prefix xor of pref ----------
        # We store the difference array d such that:
        #   d[1] = pref[euler[0]]
        #   d[i] = pref[euler[i-1]] ^ pref[euler[i-2]]  for i>1
        # Then point query at i gives pref[euler[i-1]].
        class BIT:
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 2)

            def add(self, idx, val):
                while idx <= self.n:
                    self.bit[idx] ^= val
                    idx += idx & -idx

            def prefix_xor(self, idx):
                res = 0
                while idx > 0:
                    res ^= self.bit[idx]
                    idx -= idx & -idx
                return res

            def point_query(self, idx):
                return self.prefix_xor(idx)

        bit = BIT(n)
        # initialise with d
        bit.add(1, pref[euler[0]])
        for i in range(2, n + 1):
            bit.add(i, pref[euler[i - 1]] ^ pref[euler[i - 2]])

        # ---------- LCA ----------
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            k = 0
            while diff:
                if diff & 1:
                    u = up[k][u]
                diff >>= 1
                k += 1
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
            return up[0][u]

        # ---------- process queries ----------
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_mask = 1 << (ord(c) - 97)
                old_mask = val_mask[u]
                if old_mask != new_mask:
                    delta = old_mask ^ new_mask
                    # update difference array at boundaries of subtree
                    bit.add(tin[u] + 1, delta)
                    if tout[u] + 2 <= n:
                        bit.add(tout[u] + 2, delta)
                    val_mask[u] = new_mask
            else:  # query
                u = int(parts[1])
                v = int(parts[2])
                w = lca(u, v)
                pref_u = bit.point_query(tin[u] + 1)
                pref_v = bit.point_query(tin[v] + 1)
                val_w = val_mask[w]
                path_xor = pref_u ^ pref_v ^ val_w
                # palindrome iff at most one bit set
                ans.append((path_xor & (path_xor - 1)) == 0)

        return ans
