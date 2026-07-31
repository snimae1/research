from collections import Counter, deque

class Solution(object):
    def minCost(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        total_counts = Counter(nums1) + Counter(nums2)
        
        # Bedingung 1: Alle Elemente müssen insgesamt eine gerade Anzahl Male vorkommen
        for val in total_counts:
            if total_counts[val] % 2 != 0:
                return -1
        
        # Soll-Zustand für nums1: jedes Element muss genau die Hälfte des Gesamtvorkommens haben
        target = {val: count // 2 for val, count in total_counts.items()}
        current = Counter(nums1)
        
        # Berechne Balance Delta: positiv bedeutet "benötigt", negativ bedeutet "zu viel"
        # Wir bewegen Fluss von (zu viel -> benötigt)
        diff = {}
        sources = [] # Knoten mit zu vielen Elementen (Delta < 0)
        sinks = []   # Knoten die Elemente benötigen (Delta > 0)
        
        all_vals = list(total_counts.keys())
        for v in all_vals:
            delta = target[v] - current[v]
            if delta != 0:
                diff[v] = delta
                if delta < 0:
                    sources.append(v)
                else:
                    sinks.append(v)

        # Baue den Graphen aus den Paaren (u, v), wo u=nums1[i], v=nums2[i]
        # Nur Kanten zwischen unterschiedlichen Werten sind relevant
        adj = {} # Adjazenzliste für das Flussnetzwerk
        for u, v in zip(nums1, nums2):
            if u == v: continue
            if u not in adj: adj[u] = []
            # Jede Kante hat Kapazität 1 und Kosten 1
            adj[u].append([v, 1]) # [Ziel, Kapazität]

        total_cost = 0
        
        # Wir versuchen nun, die Defizite der Sinks durch Fluss von den Sources zu decken.
        # Da alle Kanten die gleichen Kosten (1) haben, ist ein BFS-basierter Ansatz optimal.
        while True:
            # Suche Source mit Delta < 0 und Sink mit Delta > 0
            src = None
            for s in sources:
                if diff.get(s, 0) < 0:
                    src = s
                    break
            
            if src is None: break # Alle’s erledigt oder unmöglich
            
            # BFS um den kürzesten Pfad von der Source zu irgendeinem Sink zu finden
            queue = deque([(src, [])])
            visited = {src}
            found_path = None
            
            while queue:
                curr, path = queue.popleft()
                
                if curr in diff and diff[curr] > 0:
                    found_path = (curr, path)
                    break
                
                if curr in adj:
                    for neighbor_info in adj[curr]:
                        neighbor, cap = neighbor_info
                        if cap > 0 and neighbor not in visited:
                            visited.add(neighbor)
                            queue.append((neighbor, path + [neighbor_info]))
            
            if found_path:
                sink, path_edges = found_path
                # Flussmenge bestimmen (wie viel kann maximal bewegt werden?)
                flow = min(-diff[src], diff[sink])
                # Da Kapazitäten pro Kante 1 sind, bewegen wir meistens nur 1 Einheit
                # Aber wir prüfen die Kantenkapazität im Pfad:
                for edge in path_edges:
                    flow = min(flow, edge[1])
                
                total_cost += flow * len(path_edges)
                diff[src] += flow
                diff[sink] -= flow
                # Kapazitäten aktualisieren
                for edge in path_edges:
                    edge[1] -= flow
            else:
                # Keine Pfade mehr von dieser Source zu irgendeinem Sink möglich
                # Wir entfernen die Source aus der Liste, um Endlosschleifen zu vermeiden
                sources.remove(src)

        # Finaler Check: Sind alle Differenzen auf 0?
        for v in diff:
            if diff[v] != 0:
                return -1
                
        return total_cost
