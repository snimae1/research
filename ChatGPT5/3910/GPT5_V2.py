"""Count connected node subsets with an even sum of node values."""

class Solution:
"""Solve the even-sum connected subgraph problem."""

```
def evenSumSubgraphs(self, nums, edges):  # pylint: disable=invalid-name
    """
    Count non-empty connected subsets whose node-value sum is even.

    :param nums: List containing 0 or 1 for every node.
    :param edges: Undirected edges of the graph.
    :return: Number of valid non-empty subsets.
    """
    graph = self._build_graph(len(nums), edges)
    result = 0

    # Try every possible non-empty subset of nodes.
    for subset in range(1, 1 << len(nums)):
        if self._has_even_sum(subset, nums) and \
                self._is_connected(subset, graph):
            result += 1

    return result

@staticmethod
def _build_graph(node_count, edges):
    """Build the graph using one bit mask per node."""
    graph = [0] * node_count

    for first, second in edges:
        graph[first] |= 1 << second
        graph[second] |= 1 << first

    return graph

@staticmethod
def _has_even_sum(subset, nums):
    """Return True if the values in the subset have an even sum."""
    parity = 0
    remaining = subset

    # XOR gives the parity of the sum:
    # 0 = even, 1 = odd.
    while remaining:
        lowest_bit = remaining & -remaining
        node = lowest_bit.bit_length() - 1
        parity ^= nums[node]
        remaining -= lowest_bit

    return parity == 0

@staticmethod
def _is_connected(subset, graph):
    """Return True if the induced subgraph is connected."""
    # Start with any node contained in the subset.
    start = subset & -subset
    visited = start
    stack = start

    # Traverse only nodes that belong to the current subset.
    while stack:
        current_bit = stack & -stack
        stack -= current_bit

        node = current_bit.bit_length() - 1
        neighbours = graph[node] & subset & ~visited

        visited |= neighbours
        stack |= neighbours

    return visited == subset
```
