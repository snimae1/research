"""
Module to solve the maxActivated problem.
This module finds the maximum number of points that can be activated
by adding one additional point.
"""

# pylint: disable=too-few-public-methods
class Solution:
    """
    Provides a method to calculate the maximum number of activated points
    using a Disjoint Set Union (DSU) approach.
    """

    # pylint: disable=invalid-name
    def maxActivated(self, points):
        """
        Calculates the maximum points activated including the newly added point.

        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n == 0:
            return 1

        # DSU structures: parent for connectivity, size for component weight
        parent = list(range(n))
        size = [1] * n

        def find(i):
            """Finds the root of the component with path compression (iterative)."""
            root = i
            while parent[root] != root:
                root = parent[root]
            # Path compression for future efficiency
            while parent[i] != root:
                next_node = parent[i]
                parent[i] = root
                i = next_node
            return root

        def union(i, j):
            """Merges two components using union by size."""
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                if size[root_i] < size[root_j]:
                    root_i, root_j = root_j, root_i
                parent[root_j] = root_i
                size[root_i] += size[root_j]

        # Maps to group indices by their x and y coordinates
        x_map = {}
        y_map = {}

        for i in range(n):
            x, y = points[i]

            # Connect points sharing the same x-coordinate
            if x in x_map:
                union(i, x_map[x])
            else:
                x_map[x] = i

            # Connect points sharing the same y-coordinate
            if y in y_map:
                union(i, y_map[y])
            else:
                y_map[y] = i

        # Extract sizes of all unique connected components
        component_sizes = []
        for i in range(n):
            if parent[i] == i:
                component_sizes.append(size[i])

        # Sort sizes descending to easily pick the two largest components
        component_sizes.sort(reverse=True)

        # We can bridge the two largest components by placing the new point
        # at (x_from_comp1, y_from_comp2).
        if len(component_sizes) >= 2:
            return 1 + component_sizes[0] + component_sizes[1]

        # If only one component exists, we just add the new point to it
        return 1 + component_sizes[0]
