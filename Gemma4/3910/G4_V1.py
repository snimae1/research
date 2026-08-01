class Solution(object):

    def evenSumSubgraphs(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        # Erstelle eine Adjazenzliste für den Graphen
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count = 0
        
        # Es gibt 2^n mögliche Teilmengen. Wir iterieren von 1 bis 2^n - 1, 
        # um die leere Menge auszuschließen.
        for mask in range(1, 1 << n):
            subset = []
            current_sum = 0
            
            # Bestimme, welche Knoten in der aktuellen Teilmenge (mask) sind
            for i in range(n):
                if (mask >> i) & 1:
                    subset.append(i)
                    current_sum += nums[i]
            
            # Bedingung 2: Die Summe der Werte muss gerade sein
            if current_sum % 2 == 0:
                # Bedingung 1: Der induzierte Subgraph muss zusammenhängend sein
                if self.is_connected(subset, adj):
                    count += 1
                    
        return count

    def is_connected(self, subset, adj):
        if not subset:
            return False
        
        # Wir starten eine BFS/DFS von einem beliebigem Knoten in der Teilmenge
        start_node = subset[0]
        visited = {start_node}
        stack = [start_node]
        subset_set = set(subset)
        
        while stack:
            u = stack.pop()
            for v in adj[u]:
                # Wir besuchen den Nachbarn nur, wenn er Teil der gewählten Teilmenge ist
                # und noch nicht besucht wurde
                if v in subset_set and v not in visited:
                    visited.add(v)
                    stack.append(v)
        
        # Wenn die Anzahl der besuchten Knoten gleich der Größe der Teilmenge ist,
        # ist der induzierte Subgraph zusammenhängend.
        return len(visited) == len(subset)
