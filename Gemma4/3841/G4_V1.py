import sys

# Erhöhung des Rekursionslimits für tiefe Bäume
sys.setrecursionlimit(100000)

class Solution(object):

    def palindromePath(self, n, edges, s, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type s: str
        :type queries: List[str]
        :rtype: List[bool]
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # HLD Variablen
        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n
        
        # 1. DFS zur Berechnung von Subtree-Größen und Heavy-Edges
        stack = [(0, -1, 0)] # node, p, d
        order = []
        while stack:
            u, p, d = stack.pop()
            parent[u] = p
            depth[u] = d
            order.append(u)
            for v in adj[u]:
                if v != p:
                    stack.append((v, u, d + 1))
        
        # Rückwärts durch die Order gehen, um Größen zu berechnen (Bottom-Up)
        for u in reversed(order):
            p = parent[u]
            if p != -1:
                size[p] += size[u]
                if heavy[p] == -1 or size[u] > size[heavy[p]]:
                    heavy[p] = u

        # 2. DFS zur Zuweisung von Kettenköpfen und Positionen im BIT
        head = [i for i in range(n)]
        pos = [0] * n
        current_pos = 0
        
        # Iterativer Ansatz für HLD-Dekomposition, um Rekursion zu vermeiden
        stack = [(0, 0)] # node, head_node
        while stack:
            u, h = stack.pop()
            head[u] = h
            pos[u] = current_pos
            current_pos += 1
            
            # Heavy-Child zuerst auf den Stack legen (damit es als erstes verarbeitet wird),
            # aber da es ein Stack ist, müssen wir die Light-Children zuerst pushen.
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    stack.append((v, v))
            if heavy[u] != -1:
                stack.append((heavy[u], h))

        # BIT Implementierung für XOR-Summen
        bit = [0] * (n + 1)

        def bit_update(i, delta):
            i += 1 # 1-indexed
            while i <= n:
                bit[i] ^= delta
                i += i & (-i)

        def bit_query(i):
            i += 1 # 1-indexed
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & (-i)
            return res

        def get_range_xor(l, r):
            return bit_query(r) ^ bit_query(l - 1)

        # Initialisierung des BIT mit den Anfangswerten von s
        current_chars = [ord(c) - ord('a') for c in s]
        for i in range(n):
            bit_update(pos[i], 1 << current_chars[i])

        def query_path(u, v):
            res_mask = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                res_mask ^= get_range_xor(pos[head[u]], pos[u])
                u = parent[head[u]]
            
            if depth[u] > depth[v]:
                u, v = v, u
            res_mask ^= get_range_xor(pos[u], pos[v])
            return res_mask

        # Verarbeitung der Queries
        results = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_char_idx = ord(parts[2]) - ord('a')
                # XOR-Update: Altes Bit entfernen, neues hinzufügen
                old_mask = 1 << current_chars[u]
                new_mask = 1 << new_char_idx
                bit_update(pos[u], old_mask ^ new_mask)
                current_chars[u] = new_char_idx
            else:
                u, v = int(parts[1]), int(parts[2])
                mask = query_path(u, v)
                # Ein Palindrom ist möglich, wenn höchstens ein Bit gesetzt ist
                # (mask & (mask - 1)) == 0 prüft genau das
                results.append((mask & (mask - 1)) == 0)

        return results
