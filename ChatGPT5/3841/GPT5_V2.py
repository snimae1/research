"""Efficiently process palindrome-permutation queries on paths in a tree."""


class SegmentTree:
    """Segment tree that combines character parity masks using XOR."""

    def __init__(self, values):
        """Initialize the segment tree with the given values."""
        self.length = len(values)
        self.tree_size = self._next_power_of_two(self.length)
        self.tree = [0] * (2 * self.tree_size)
        self._build(values)

    @staticmethod
    def _next_power_of_two(length):
        """Return the smallest power of two greater than or equal to length."""
        size = 1
        while size < length:
            size <<= 1
        return size

    def _build(self, values):
        """Build the tree from the initial values."""
        for index, value in enumerate(values):
            self.tree[self.tree_size + index] = value

        for index in range(self.tree_size - 1, 0, -1):
            self.tree[index] = (
                self.tree[index * 2] ^ self.tree[index * 2 + 1]
            )

    def update(self, index, value):
        """Replace the value at index."""
        index += self.tree_size
        self.tree[index] = value

        index //= 2
        while index:
            self.tree[index] = (
                self.tree[index * 2] ^ self.tree[index * 2 + 1]
            )
            index //= 2

    def query(self, left, right):
        """Return the XOR value for the inclusive range [left, right]."""
        result = 0
        left += self.tree_size
        right += self.tree_size

        while left <= right:
            if left % 2 == 1:
                result ^= self.tree[left]
                left += 1

            if right % 2 == 0:
                result ^= self.tree[right]
                right -= 1

            left //= 2
            right //= 2

        return result


class HeavyLightDecomposition:
    """Represent tree paths as a small number of contiguous array ranges."""

    def __init__(self, graph):
        """Create a heavy-light decomposition for the given tree."""
        self.graph = graph
        self.node_count = len(graph)

        self.parent = [-1] * self.node_count
        self.depth = [0] * self.node_count
        self.subtree_size = [0] * self.node_count
        self.heavy_child = [-1] * self.node_count

        self.chain_head = [0] * self.node_count
        self.position = [0] * self.node_count

        self._build()

    def _build(self):
        """Build parent, subtree and heavy-light information."""
        traversal_order = self._build_parent_and_depth()
        self._find_heavy_children(traversal_order)
        self._assign_positions()

    def _build_parent_and_depth(self):
        """Iteratively traverse the tree and determine parents and depths."""
        order = []
        stack = [0]
        self.parent[0] = 0

        while stack:
            node = stack.pop()
            order.append(node)

            for neighbor in self.graph[node]:
                if neighbor == self.parent[node]:
                    continue

                self.parent[neighbor] = node
                self.depth[neighbor] = self.depth[node] + 1
                stack.append(neighbor)

        return order

    def _find_heavy_children(self, traversal_order):
        """Calculate subtree sizes and select the largest child as heavy."""
        for node in reversed(traversal_order):
            self.subtree_size[node] = 1
            largest_subtree = 0

            for neighbor in self.graph[node]:
                if neighbor == self.parent[node]:
                    continue

                self.subtree_size[node] += self.subtree_size[neighbor]

                if self.subtree_size[neighbor] > largest_subtree:
                    largest_subtree = self.subtree_size[neighbor]
                    self.heavy_child[node] = neighbor

    def _assign_positions(self):
        """Assign each node a position in the heavy-light base array."""
        current_position = 0
        stack = [(0, 0)]

        while stack:
            node, head = stack.pop()

            while node != -1:
                self.chain_head[node] = head
                self.position[node] = current_position
                current_position += 1

                self._add_light_children_to_stack(stack, node)

                node = self.heavy_child[node]

    def _add_light_children_to_stack(self, stack, node):
        """Add all light children of node as new chains."""
        for neighbor in reversed(self.graph[node]):
            if neighbor not in (
                self.parent[node],
                self.heavy_child[node],
            ):
                stack.append((neighbor, neighbor))

    def path_ranges(self, first_node, second_node):
        """Yield the array ranges representing the path between two nodes."""
        while (
            self.chain_head[first_node]
            != self.chain_head[second_node]
        ):
            if (
                self.depth[self.chain_head[first_node]]
                < self.depth[self.chain_head[second_node]]
            ):
                first_node, second_node = second_node, first_node

            yield (
                self.position[self.chain_head[first_node]],
                self.position[first_node],
            )

            first_node = self.parent[self.chain_head[first_node]]

        left = min(
            self.position[first_node],
            self.position[second_node],
        )
        right = max(
            self.position[first_node],
            self.position[second_node],
        )

        yield left, right


class Solution:
    """Solve dynamic palindrome-permutation queries on tree paths."""

    def palindromePath(self, n, edges, s, queries):
        """
        Process updates and determine whether path characters form a palindrome.

        A path can be rearranged into a palindrome when at most one character
        occurs an odd number of times.
        """
        graph = self._build_graph(n, edges)
        decomposition = HeavyLightDecomposition(graph)

        characters = list(s)
        values = self._build_initial_values(
            characters,
            decomposition.position,
            n,
        )

        segment_tree = SegmentTree(values)
        answers = []

        for query in queries:
            command = query.split()

            if command[0] == "update":
                self._process_update(
                    command,
                    characters,
                    decomposition,
                    segment_tree,
                )
            else:
                answers.append(
                    self._process_path_query(
                        command,
                        decomposition,
                        segment_tree,
                    )
                )

        return answers

    @staticmethod
    def _build_graph(node_count, edges):
        """Create an adjacency list for the undirected tree."""
        graph = [[] for _ in range(node_count)]

        for first_node, second_node in edges:
            graph[first_node].append(second_node)
            graph[second_node].append(first_node)

        return graph

    @staticmethod
    def _character_mask(character):
        """Return the parity bit mask representing one lowercase character."""
        return 1 << (ord(character) - ord("a"))

    def _build_initial_values(self, characters, positions, node_count):
        """Create the base array used by the segment tree."""
        values = [0] * node_count

        for node in range(node_count):
            values[positions[node]] = self._character_mask(
                characters[node]
            )

        return values

    def _process_update(
        self,
        command,
        characters,
        decomposition,
        segment_tree,
    ):
        """Update one node and its corresponding segment-tree value."""
        node = int(command[1])
        character = command[2]

        characters[node] = character

        segment_tree.update(
            decomposition.position[node],
            self._character_mask(character),
        )

    def _process_path_query(
        self,
        command,
        decomposition,
        segment_tree,
    ):
        """Determine whether the characters on a path can form a palindrome."""
        first_node = int(command[1])
        second_node = int(command[2])

        parity_mask = 0

        for left, right in decomposition.path_ranges(
            first_node,
            second_node,
        ):
            parity_mask ^= segment_tree.query(left, right)

        return self._has_at_most_one_bit(parity_mask)

    @staticmethod
    def _has_at_most_one_bit(value):
        """Return whether zero or one bits are set in value."""
        return value == 0 or value & (value - 1) == 0
