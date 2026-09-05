"""
Solution for the maximum activated points problem.
"""

class Solution:
    """
    Provides a method to compute the maximum number of activatable points
    after adding one extra point.
    """

    @staticmethod
    def _find(parent, i):
        """Find with path compression."""
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    @staticmethod
    def _union(parent, i, j):
        """Union by setting root of i to root of j."""
        ri = Solution._find(parent, i)
        rj = Solution._find(parent, j)
        if ri != rj:
            parent[ri] = rj

    def max_activated(self, points):
        """
        Compute the maximum number of points that can be activated,
        including a newly added point.

        :param points: List of [x, y] coordinates, distinct.
        :return: Maximum activatable points count.
        """
        # Extract unique x and y coordinates.
        xs = set()
        ys = set()
        for x, y in points:
            xs.add(x)
            ys.add(y)

        # Map coordinates to unique node indices in a bipartite graph.
        x_to_idx = {x: i for i, x in enumerate(xs)}
        offset = len(xs)
        y_to_idx = {y: i + offset for i, y in enumerate(ys)}

        n_nodes = len(xs) + len(ys)
        parent = list(range(n_nodes))

        # Union x and y of each point to connect components.
        for x, y in points:
            Solution._union(parent, x_to_idx[x], y_to_idx[y])

        # Compress paths to get final roots.
        for i in range(n_nodes):
            parent[i] = Solution._find(parent, i)

        # Count points (edges) per connected component.
        comp_size = [0] * n_nodes
        for x, _ in points:
            root = parent[x_to_idx[x]]
            comp_size[root] += 1

        sizes = [s for s in comp_size if s > 0]

        # If only one component, adding a point activates all existing points + new point.
        if len(sizes) == 1:
            return len(points) + 1

        # Otherwise we can connect the two largest components with one added point.
        sizes.sort(reverse=True)
        return sizes[0] + sizes[1] + 1

    # pylint: disable=invalid-name
    def maxActivated(self, points):
        """
        Wrapper for LeetCode-style naming convention.
        Calls max_activated.
        """
        return self.max_activated(points)
