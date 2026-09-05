"""
 Dieses Modul bietet eine Lösung zur Berechnung der minimalen Kosten, 
 um zwei Arrays durch Tauschoperationen identisch zu machen.
"""
from collections import Counter, deque

class Solution(object):
    """
    Klasse zur Lösung des Problems der minimalen Tauschkosten 
    zwischen zwei Arrays.
    """

    def minCost(self, nums1, nums2):
        """
        Berechnet die minimalen Kosten, um nums1 und nums2 identisch zu machen.
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        total_counts = Counter(nums1) + Counter(nums2)

        if not self._is_possible(total_counts):
            return -1

        target = {val: count // 2 for val, count in total_counts.items()}
        current = Counter(nums1)
        diff, sources, sinks = self._calculate_balance(target, current)
        adj = self._build_graph(nums1, nums2)

        return self._solve_min_cost(diff, sources, sinks, adj)

    def _is_possible(self, total_counts):
        """Prüft, ob jedes Element insgesamt eine gerade Anzahl Male vorkommt."""
        for count in total_counts.values():
            if count % 2 != 0:
                return False
        return True

    def _calculate_balance(self, target, current):
        """Berechnet die Differenzen zwischen Ist- und Soll-Zustand."""
        diff = {}
        sources = []
        sinks = []
        for val, target_count in target.items():
            delta = target_count - current.get(val, 0)
            if delta != 0:
                diff[val] = delta
                if delta < 0:
                    sources.append(val)
                else:
                    sinks.append(val)
        return diff, sources, sinks

    def _build_graph(self, nums1, nums2):
        """Erstellt den Graphen der möglichen Tauschoperationen."""
        adj = {}
        for u, v in zip(nums1, nums2):
            if u == v:
                continue
            if u not in adj:
                adj[u] = []
            # [Ziel, Kapazität]
            adj[u].append([v, 1])
        return adj

    def _find_path(self, src, diff, adj):
        """Findet mittels BFS den kürzesten Pfad von einer Source zu einem Sink."""
        queue = deque([(src, [])])
        visited = {src}

        while queue:
            curr, path = queue.popleft()

            # Wenn der aktuelle Knoten ein Sink ist (Delta > 0)
            if diff.get(curr, 0) > 0:
                return curr, path

            if curr in adj:
                for neighbor_info in adj[curr]:
                    neighbor, cap = neighbor_info
                    if cap > 0 and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, path + [neighbor_info]))
        return None, None

    def _solve_min_cost(self, diff, sources, sinks, adj):
        """Orchestriert den Fluss-Algorithmus zur Kostenberechnung."""
        total_cost = 0
        # Wir kopieren die Quellenliste, um sie sicher modifizieren zu können
        active_sources = list(sources)

        while active_sources:
            src = active_sources[0]
            if diff.get(src, 0) >= 0:
                active_sources.pop(0)
                continue

            sink, path_edges = self._find_path(src, diff, adj)

            if sink:
                # Maximiere den Fluss für diesen Pfad
                flow = min(-diff[src], diff[sink])
                for edge in path_edges:
                    flow = min(flow, edge[1])

                total_cost += flow * len(path_edges)
                diff[src] += flow
                diff[sink] -= flow
                for edge in path_edges:
                    edge[1] -= flow
            else:
                # Keine Pfade mehr von dieser Quelle möglich
                active_sources.pop(0)

        # Finaler Check: Sind alle Defizite behoben?
        for val, delta in diff.items():
            if delta != 0:
                return -1
        return total_cost
