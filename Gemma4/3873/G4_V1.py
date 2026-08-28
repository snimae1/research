class Solution(object):
    def maxActivated(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Disjoint Set Union (DSU) Struktur zur Verwaltung der Komponenten
        parent = {}

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        # Wir müssen X- und Y-Koordinaten unterscheiden. 
        # Da Koordinaten identisch sein können (z.B. x=1 und y=1),
        # markieren wir X-Koordinaten mit einem Präfix oder Tuple.
        for x, y in points:
            x_node = ('x', x)
            y_node = ('y', y)
            
            if x_node not in parent: parent[x_node] = x_node
            if y_node not in parent: parent[y_node] = y_node
            
            union(x_node, y_node)

        # Zähle, wie viele ursprüngliche Punkte zu jeder Komponente gehören
        component_sizes = {}
        for x, y in points:
            # Jedes Punkt-Paar gehört zur Komponente seines Repräsentanten (root)
            root = find(('x', x))
            component_sizes[root] = component_sizes.get(root, 0) + 1

        # Extrahiere die Größen aller gefundenen Komponenten
        sizes = sorted(component_sizes.values(), reverse=True)

        # Fall 1: Es gibt zwei oder mehr Komponenten.
        # Wir verbinden die zwei größten Komponenten mit einem neuen Punkt.
        if len(sizes) >= 2:
            return sizes[0] + sizes[1] + 1
        
        # Fall 2: Es gibt nur eine Komponente.
        # Wir fügen einen Punkt hinzu, der an diese eine Komponente anschließt.
        elif len(sizes) == 1:
            return sizes[0] + 1
        
        # Fall 3: Keine Punkte vorhanden (laut Constraints nicht möglich, aber zur Sicherheit)
        else:
            return 1
