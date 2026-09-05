"""
Dieses Modul bietet eine Lösung zur Überprüfung von Palindrom-Pfaden in einem Baum.
Es verwendet Heavy-Light Decomposition (HLD) und einen Binary Indexed Tree (BIT),
um Pfadanfragen und Punkt-Updates in O(log^2 n) Zeitkomplexität zu bearbeiten.
"""

import sys

# Erhöhung des Rekursionslimits für sehr tiefe Bäume
sys.setrecursionlimit(100000)


class FenwickTree:
    """Implementation eines Binary Indexed Tree (BIT) für XOR-Summen."""

    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, i, delta):
        """Aktualisiert den Wert an Position i mittels XOR."""
        i += 1  # Umwandlung in 1-basierte Indexierung
        while i < len(self.tree):
            self.tree[i] ^= delta
            i += i & (-i)

    def query(self, i):
        """Berechnet die XOR-Präfixsumme bis Position i."""
        i += 1
        res = 0
        while i > 0:
            res ^= self.tree[i]
            i -= i & (-i)
        return res

    def query_range(self, left, right):
        """Berechnet die XOR-Summe im Bereich [left, right]."""
        return self.query(right) ^ self.query(left - 1)


class TreeManager:
    """Verwaltet die Baumstruktur, HLD-Positionen und Pfadabfragen."""

    def __init__(self, n, edges, s):
        self.n = n
        self.adj = [[] for _ in range(n)]
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)

        self.parent = [-1] * n
        self.depth = [0] * n
        self.size = [1] * n
        self.heavy = [-1] * n
        self.head = list(range(n))
        self.pos = [0] * n
        self.bit = FenwickTree(n)

        self._build_hld(s)

    def _build_hld(self, s):
        """Initialisiert HLD und den BIT in mehreren Durchgängen."""
        # 1. DFS: Größen und Heavy-Edges berechnen (iterativ)
        stack = [(0, -1, 0)]
        order = []
        while stack:
            u, p, d = stack.pop()
            self.parent[u] = p
            self.depth[u] = d
            order.append(u)
            for v in self.adj[u]:
                if v != p:
                    stack.append((v, u, d + 1))

        for u in reversed(order):
            p = self.parent[u]
            if p != -1:
                self.size[p] += self.size[u]
                if self.heavy[p] == -1 or self.size[u] > self.size[self.heavy[p]]:
                    self.heavy[p] = u

        # 2. DFS: Kettenköpfe und BIT-Positionen zuweisen (iterativ)
        curr_pos = 0
        stack = [(0, 0)]  # node, head_node
        while stack:
            u, h = stack.pop()
            self.head[u] = h
            self.pos[u] = curr_pos
            curr_pos += 1

            # Light-Children zuerst, damit Heavy-Child zuerst verarbeitet wird
            for v in self.adj[u]:
                if v != self.parent[u] and v not in (self.heavy[u], -1):
                    stack.append((v, v))
            if self.heavy[u] != -1:
                stack.append((self.heavy[u], h))

        # Initialisierung des BIT mit den Zeichen-Masken
        for i in range(self.n):
            mask = 1 << (ord(s[i]) - ord('a'))
            self.bit.update(self.pos[i], mask)

    def update_node(self, u, old_char, new_char):
        """Aktualisiert den Zeichenwert eines Knotens im BIT."""
        old_mask = 1 << (ord(old_char) - ord('a'))
        new_mask = 1 << (ord(new_char) - ord('a'))
        self.bit.update(self.pos[u], old_mask ^ new_mask)

    def query_path(self, u, v):
        """Berechnet die XOR-Summe der Zeichen auf dem Pfad zwischen u und v."""
        res_mask = 0
        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] < self.depth[self.head[v]]:
                u, v = v, u
            res_mask ^= self.bit.query_range(self.pos[self.head[u]], self.pos[u])
            u = self.parent[self.head[u]]

        if self.depth[u] > self.depth[v]:
            u, v = v, u
        res_mask ^= self.bit.query_range(self.pos[u], self.pos[v])
        return res_mask


class Solution:
    """Lösungsklasse für die Palindrom-Pfad-Abfrage."""

    def palindromePath(self, n, edges, s, queries):
        """
        Prüft, ob Pfade in einem Baum zu Palindromen umgestellt werden können.

        :param n: Anzahl der Knoten
        :param edges: Liste der Kanten [u, v]
        :param s: String der Knotenwerte
        :param queries: Liste von "update ui c" oder "query ui vi"
        :return: Liste von Booleans für jede "query"-Anfrage
        """
        tree = TreeManager(n, edges, s)
        current_s = list(s)
        results = []

        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u, char = int(parts[1]), parts[2]
                tree.update_node(u, current_s[u], char)
                current_s[u] = char
            else:
                u, v = int(parts[1]), int(parts[2])
                mask = tree.query_path(u, v)
                # Palindrom-Bedingung: Max ein Bit darf gesetzt sein
                results.append((mask & (mask - 1)) == 0)

        return results
