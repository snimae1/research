class Solution(object):
    def maxActivated(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # collect distinct x and y coordinates
        xs = set()
        ys = set()
        for x, y in points:
            xs.add(x)
            ys.add(y)

        # map x and y to unique node indices
        x_list = list(xs)
        y_list = list(ys)
        x_to_idx = {x: i for i, x in enumerate(x_list)}
        # y indices start after x indices to keep them separate
        offset = len(x_list)
        y_to_idx = {y: i + offset for i, y in enumerate(y_list)}

        n_nodes = len(x_list) + len(y_list)
        parent = list(range(n_nodes))

        def find(i):
            # path compression
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        def union(i, j):
            ri, rj = find(i), find(j)
            if ri != rj:
                parent[ri] = rj

        # build graph components by unioning x and y of each point
        for x, y in points:
            u = x_to_idx[x]
            v = y_to_idx[y]
            union(u, v)

        # compress all paths
        for i in range(n_nodes):
            parent[i] = find(i)

        # count edges (points) per component
        comp_size = [0] * n_nodes
        for x, y in points:
            root = parent[x_to_idx[x]]
            comp_size[root] += 1

        sizes = [s for s in comp_size if s > 0]
        # if only one component, we can always add one point to activate all
        if len(sizes) == 1:
            return len(points) + 1

        # otherwise we can connect the two largest components
        sizes.sort(reverse=True)
        return sizes[0] + sizes[1] + 1
