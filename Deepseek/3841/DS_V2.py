"""
Solution for "Palindrome Path" problem using binary lifting, prefix XOR, and Fenwick tree.
"""

from typing import List


class Solution:
    """
    Provides method palindromePath to answer queries on a tree with character updates.
    """

    def palindromePath(self, n: int, edges: List[List[int]], s: str,
                       queries: List[str]) -> List[bool]:
        """
        Process path palindrome queries with point updates on node characters.

        Args:
            n: Number of nodes.
            edges: Tree edges.
            s: Initial string of characters on nodes.
            queries: List of "update" or "query" strings.

        Returns:
            List of boolean answers for each "query" in the original order.
        """
        # Preprocess tree structure and binary lifting tables
        adj, depth, up, tin, tout, euler, pref, val_mask = self._build_tree(n, edges, s)

        # Fenwick tree over Euler tour to support subtree XOR updates
        bit = self._build_fenwick(n, euler, pref)

        # Process each query
        answers = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_char = parts[2]
                self._apply_update(u, new_char, val_mask, tin, tout, bit)
            else:  # "query"
                u = int(parts[1])
                v = int(parts[2])
                ans = self._answer_query(u, v, val_mask, tin, bit, up, depth)
                answers.append(ans)
        return answers

    # ----------------------------------------------------------------------
    # Private helpers
    # ----------------------------------------------------------------------

    def _build_tree(self, n: int, edges: List[List[int]], s: str):
        """Build adjacency, compute DFS order, depths, binary lifting table and prefix XORs."""
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        val_mask = [1 << (ord(ch) - 97) for ch in s]

        log_bits = (n).bit_length()
        up = [[0] * n for _ in range(log_bits)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        pref = [0] * n
        euler = [0] * n

        timer = 0
        stack = [(0, -1, 0)]  # (node, parent, state) 0=enter, 1=exit
        while stack:
            node, parent, state = stack.pop()
            if state == 0:
                tin[node] = timer
                euler[timer] = node
                timer += 1

                up[0][node] = parent if parent != -1 else node
                if parent == -1:
                    depth[node] = 0
                    pref[node] = val_mask[node]
                else:
                    depth[node] = depth[parent] + 1
                    pref[node] = pref[parent] ^ val_mask[node]

                stack.append((node, parent, 1))
                for nei in reversed(adj[node]):
                    if nei != parent:
                        stack.append((nei, node, 0))
            else:
                tout[node] = timer - 1

        # Fill binary lifting table
        for k in range(1, log_bits):
            prev = up[k - 1]
            cur = up[k]
            for v in range(n):
                cur[v] = prev[prev[v]]

        return adj, depth, up, tin, tout, euler, pref, val_mask

    # ----------------------------------------------------------------------

    class _FenwickXor:
        """Fenwick tree for XOR prefix queries (point update, prefix XOR)."""

        def __init__(self, size: int):
            self.n = size
            self.bit = [0] * (size + 2)

        def add(self, idx: int, value: int) -> None:
            """Add value to position idx (1‑based)."""
            while idx <= self.n:
                self.bit[idx] ^= value
                idx += idx & -idx

        def prefix(self, idx: int) -> int:
            """XOR of elements 1..idx."""
            res = 0
            while idx > 0:
                res ^= self.bit[idx]
                idx -= idx & -idx
            return res

        def point_query(self, idx: int) -> int:
            """Get value at position idx (1‑based)."""
            return self.prefix(idx)

    # ----------------------------------------------------------------------

    def _build_fenwick(self, n: int, euler: List[int], pref: List[int]):
        """Initialise Fenwick tree with difference array over Euler order."""
        bit = self._FenwickXor(n)
        bit.add(1, pref[euler[0]])
        for i in range(2, n + 1):
            bit.add(i, pref[euler[i - 1]] ^ pref[euler[i - 2]])
        return bit

    # ----------------------------------------------------------------------

    def _apply_update(self, u: int, new_char: str, val_mask: List[int],
                      tin: List[int], tout: List[int], bit) -> None:
        """Change character at node u and update the Fenwick tree accordingly."""
        new_mask = 1 << (ord(new_char) - 97)
        old_mask = val_mask[u]
        if old_mask != new_mask:
            delta = old_mask ^ new_mask
            # Update subtree range [tin[u], tout[u]] in Euler order (1‑based)
            bit.add(tin[u] + 1, delta)
            if tout[u] + 2 <= bit.n:
                bit.add(tout[u] + 2, delta)
            val_mask[u] = new_mask

    # ----------------------------------------------------------------------

    def _lca(self, u: int, v: int, up: List[List[int]], depth: List[int]) -> int:
        """Return lowest common ancestor of u and v using binary lifting."""
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
        for k in range(len(up) - 1, -1, -1):
            if up[k][u] != up[k][v]:
                u = up[k][u]
                v = up[k][v]
        return up[0][u]

    # ----------------------------------------------------------------------

    def _answer_query(self, u: int, v: int, val_mask: List[int],
                      tin: List[int], bit, up: List[List[int]], depth: List[int]) -> bool:
        """Check if the path u->v can be rearranged into a palindrome."""
        w = self._lca(u, v, up, depth)
        # current prefix XOR values at nodes u and v
        pref_u = bit.point_query(tin[u] + 1)
        pref_v = bit.point_query(tin[v] + 1)
        val_w = val_mask[w]
        path_xor = pref_u ^ pref_v ^ val_w
        # Palindrome iff at most one bit set in the parity mask
        return (path_xor & (path_xor - 1)) == 0
