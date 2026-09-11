"""Find the maximum number of points that can be activated."""


class Solution:
    """Solve the point activation problem."""

    def maxActivated(self, points):
        """
        Return the maximum number of activated points.

        :param points: List of [x, y] coordinates.
        :return: Maximum number of activated points.
        """
        parent = {}
        component_size = {}

        def find(node):
            """Find the representative of a component."""
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(first, second):
            """Merge two connected components."""
            root_first = find(first)
            root_second = find(second)

            if root_first == root_second:
                return

            if component_size[root_first] < component_size[root_second]:
                root_first, root_second = root_second, root_first

            parent[root_second] = root_first
            component_size[root_first] += component_size[root_second]

        # Every x- and y-coordinate is represented by a graph node.
        # Each point connects its x-coordinate with its y-coordinate.
        for x_value, y_value in points:
            x_node = ("x", x_value)
            y_node = ("y", y_value)

            if x_node not in parent:
                parent[x_node] = x_node
                component_size[x_node] = 0

            if y_node not in parent:
                parent[y_node] = y_node
                component_size[y_node] = 0

            component_size[x_node] += 1
            component_size[y_node] += 1

            union(x_node, y_node)

        # Count the number of points in each connected component.
        points_per_component = {}

        for x_value, _ in points:
            root = find(("x", x_value))
            points_per_component[root] = (
                points_per_component.get(root, 0) + 1
            )

        # Find the two largest components.
        largest = 0
        second_largest = 0

        for count in points_per_component.values():
            if count > largest:
                second_largest = largest
                largest = count
            elif count > second_largest:
                second_largest = count

        # The new point itself is always activated.
        answer = largest + 1

        # If there are at least two components, the new point can
        # connect the two largest components.
        if second_largest > 0:
            answer = max(
                answer,
                largest + second_largest + 1
            )

        return answer
