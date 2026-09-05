```python
"""Find the maximum number of points activated by adding one point."""


class Solution:
    """Solve the point activation problem."""

    def maxActivated(self, points):
        """
        Return the maximum number of activated points.

        :param points: List of [x, y] coordinates.
        :return: Maximum number of activated points, including the new point.
        """
        parent = {}
        size = {}

        def find(value):
            """Return the representative of a component."""
            while parent[value] != value:
                parent[value] = parent[parent[value]]
                value = parent[value]
            return value

        def union(first, second):
            """Join two coordinate nodes."""
            first = find(first)
            second = find(second)

            if first == second:
                return

            if size[first] < size[second]:
                first, second = second, first

            parent[second] = first
            size[first] += size[second]

        # Each x-coordinate and y-coordinate is a graph node.
        # A point connects its x-node with its y-node.
        for x_value, y_value in points:
            x_node = ("x", x_value)
            y_node = ("y", y_value)

            if x_node not in parent:
                parent[x_node] = x_node
                size[x_node] = 0

            if y_node not in parent:
                parent[y_node] = y_node
                size[y_node] = 0

            size[x_node] += 1
            size[y_node] += 1
            union(x_node, y_node)

        # Count points belonging to every connected component.
        component_points = {}

        for x_value, y_value in points:
            root = find(("x", x_value))
            component_points[root] = component_points.get(root, 0) + 1

        # A new point can connect two existing components:
        # one through its x-coordinate and one through its y-coordinate.
        #
        # We only need to know the largest component reachable from
        # each coordinate. The total number of points in a component
        # is stored in component_points.
        x_components = {}
        y_components = {}

        for x_value, y_value in points:
            root = find(("x", x_value))
            x_components[x_value] = root
            y_components[y_value] = root

        largest = max(component_points.values())

        # Try connecting different existing components.
        # For every component, remember its largest partner.
        best_component = 0
        second_component = 0
        best_root = None

        for root, count in component_points.items():
            if count > best_component:
                second_component = best_component
                best_component = count
                best_root = root
            elif count > second_component:
                second_component = count

        # A new point can always be placed with two fresh coordinates.
        # It then activates one point only.
        answer = largest + 1

        # If there are at least two components, the new point can
        # connect the two largest components.
        if second_component > 0:
            answer = max(answer, best_component + second_component + 1)

        return answer
```
